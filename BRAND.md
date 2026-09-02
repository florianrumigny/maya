# MAYA brand guide

## Idea

The MAYA mark is a **relic in construction**. Its resolved half represents a coherent design direction. Its technical half reveals exploration, critique, alternatives, and the system that makes the direction reproducible. A structural `M` joins the two states, while amber marks the selected decision.

The symbol is contemporary and fictional. It is influenced by carved geometric rhythm without reproducing an identifiable historical or sacred Maya glyph, deity, mask, or artifact.

## Palette

| Role | Color | Hex |
|---|---|---|
| Primary ink | Graphite | `#171717` |
| Warm surface | Bone | `#F2EBDD` |
| Decision accent | Amber | `#F2A900` |
| Light presentation background | Porcelain | `#FCFAF5` |

Amber is a decision signal, not a decorative fill. Keep it below roughly 10% of the mark's visible area.

## Asset map

| Asset | Intended use |
|---|---|
| `maya-logo-primary.png` | Transparent 1024 px master for large display |
| `maya-logo-primary-512.png` | README and medium display |
| `maya-icon.png` | Simplified transparent 256 px UI icon |
| `maya-logo-symbol.svg` | Scalable simplified symbol |
| `maya-logo-monochrome.png` | One-color raster applications |
| `maya-logo-monochrome.svg` | One-color scalable applications |
| `maya-logo-on-light.png` | Ready-made porcelain-background presentation |
| `maya-logo-on-dark.png` | Ready-made graphite-background presentation |

The detailed raster mark and simplified vector symbol are intentionally different optical sizes. Do not replace the icon with a downscaled master: its construction lines will disappear.

## Usage

- Keep clear space equal to at least one eye diameter around the mark.
- Use the detailed master at 160 px or larger.
- Use the simplified symbol between 32 px and 159 px.
- Below 32 px, prefer the monochrome vector symbol.
- Keep the vertical division upright.
- Preserve the graphite, bone, and amber roles.

Do not mirror the mark, color every construction point amber, place it on a low-contrast patterned background, add effects, or redraw the two halves as unrelated faces.

## Rebuilding raster variants

The checked-in variants are generated from `maya-logo-source.png`:

```bash
python3 skills/maya/scripts/build-brand-assets.py \
  skills/maya/assets/brand/maya-logo-source.png \
  skills/maya/assets/brand
```

The script extracts the generated checkerboard, preserves real transparency, and derives the light, dark, and monochrome variants. The small icon is rendered separately from `maya-logo-symbol.svg` so it keeps its optical simplification.
