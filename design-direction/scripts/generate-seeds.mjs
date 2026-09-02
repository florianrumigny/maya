#!/usr/bin/env node

import { randomBytes } from "node:crypto";

const args = process.argv.slice(2);
const countIndex = args.indexOf("--count");
const requested = countIndex >= 0 ? Number(args[countIndex + 1]) : 3;

if (!Number.isInteger(requested) || requested < 1 || requested > 12) {
  console.error("--count must be an integer between 1 and 12");
  process.exit(1);
}

const seeds = Array.from({ length: requested }, (_, index) => {
  const raw = randomBytes(12).toString("base64url");
  const grouped = raw.match(/.{1,4}/g).join("-");
  return { direction: index + 1, seed: grouped };
});

console.log(JSON.stringify({ generatedAt: new Date().toISOString(), seeds }, null, 2));
