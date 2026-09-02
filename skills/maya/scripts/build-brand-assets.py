#!/usr/bin/env python3
"""Build MAYA's deterministic raster brand variants from the approved master art."""

from __future__ import annotations

import argparse
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter


GRAPHITE = np.array([23, 23, 23], dtype=np.uint8)
BONE = np.array([242, 235, 221], dtype=np.uint8)
AMBER = np.array([242, 169, 0], dtype=np.uint8)


def background_candidate(rgb: np.ndarray) -> np.ndarray:
    """Identify the neutral, light checkerboard without selecting the bone artwork."""
    spread = rgb.max(axis=2).astype(np.int16) - rgb.min(axis=2).astype(np.int16)
    brightness = rgb.mean(axis=2)
    return (spread <= 22) & (brightness >= 218)


def edge_connected(mask: np.ndarray) -> np.ndarray:
    height, width = mask.shape
    seen = np.zeros_like(mask, dtype=bool)
    queue: deque[tuple[int, int]] = deque()

    for x in range(width):
        if mask[0, x]:
            queue.append((0, x))
        if mask[height - 1, x]:
            queue.append((height - 1, x))
    for y in range(height):
        if mask[y, 0]:
            queue.append((y, 0))
        if mask[y, width - 1]:
            queue.append((y, width - 1))

    while queue:
        y, x = queue.popleft()
        if seen[y, x] or not mask[y, x]:
            continue
        seen[y, x] = True
        if y:
            queue.append((y - 1, x))
        if y + 1 < height:
            queue.append((y + 1, x))
        if x:
            queue.append((y, x - 1))
        if x + 1 < width:
            queue.append((y, x + 1))
    return seen


def remove_checkerboard(image: Image.Image) -> Image.Image:
    rgb = np.asarray(image.convert("RGB"))
    background = edge_connected(background_candidate(rgb))

    # Feather only the extracted boundary to avoid a pale halo.
    matte = Image.fromarray((~background * 255).astype(np.uint8), mode="L")
    matte = matte.filter(ImageFilter.GaussianBlur(0.45))
    rgba = image.convert("RGBA")
    rgba.putalpha(matte)
    return rgba


def crop_square(image: Image.Image, padding_ratio: float = 0.06) -> Image.Image:
    alpha = image.getchannel("A")
    bounds = alpha.getbbox()
    if not bounds:
        raise ValueError("The extracted artwork is empty")
    cropped = image.crop(bounds)
    side = max(cropped.size)
    padding = round(side * padding_ratio)
    canvas = Image.new("RGBA", (side + 2 * padding, side + 2 * padding))
    canvas.alpha_composite(cropped, ((canvas.width - cropped.width) // 2, (canvas.height - cropped.height) // 2))
    return canvas


def fit(image: Image.Image, size: int) -> Image.Image:
    return image.resize((size, size), Image.Resampling.LANCZOS)


def composite(image: Image.Image, color: tuple[int, int, int, int]) -> Image.Image:
    background = Image.new("RGBA", image.size, color)
    background.alpha_composite(image)
    return background


def monochrome(image: Image.Image) -> Image.Image:
    rgba = np.asarray(image.convert("RGBA"))
    rgb = rgba[:, :, :3]
    source_alpha = rgba[:, :, 3]
    luminance = rgb.mean(axis=2)
    amber = (rgb[:, :, 0] > 150) & (rgb[:, :, 1] > 75) & (rgb[:, :, 2] < 100)
    ink = (luminance < 155) | amber
    alpha = np.where(ink, source_alpha, 0).astype(np.uint8)
    result = Image.new("RGBA", image.size, (*GRAPHITE.tolist(), 0))
    result.putalpha(Image.fromarray(alpha, mode="L"))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    master = crop_square(remove_checkerboard(Image.open(args.source)))

    fit(master, 1024).save(args.output / "maya-logo-primary.png", optimize=True)
    fit(master, 512).save(args.output / "maya-logo-primary-512.png", optimize=True)
    fit(monochrome(master), 1024).save(args.output / "maya-logo-monochrome.png", optimize=True)
    composite(fit(master, 1024), (252, 250, 245, 255)).convert("RGB").save(
        args.output / "maya-logo-on-light.png"
    )
    composite(fit(master, 1024), (*GRAPHITE.tolist(), 255)).convert("RGB").save(
        args.output / "maya-logo-on-dark.png"
    )


if __name__ == "__main__":
    main()
