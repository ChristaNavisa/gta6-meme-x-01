// gta6-meme-x-01 entrypoint (Node 22, standard library only).
//
// The entry is the X post itself: the house reads the post from X (its first
// picture, the meme, then its text) and hands that to the judge. This program
// only hands the house the post's address: it copies POST.json from the
// repository root to /output/POST.json, where the gate reads it.
//
// It reads nothing else, writes nothing else, and uses no network and no
// clock, so two runs write identical bytes. It is written as plain
// JavaScript inside the .ts file, so it runs under any Node 22 or later
// with no type stripping needed.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outputDir, { recursive: true });

try {
  copyFileSync(join(botDir, "POST.json"), join(outputDir, "POST.json"));
} catch (error) {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`could not copy POST.json from ${botDir}: ${message}`);
  process.exit(1);
}
