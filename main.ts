// main.ts — gta6-meme-x-01 round 2.
// The entry is the X post named in POST.json; this program copies POST.json
// from the repository to the output directory. The house reads the post
// itself from X and builds the dossier the judge sees.
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const repoDir = process.env.MAKEFUN_BOT_DIR ?? ".";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";

const raw = readFileSync(join(repoDir, "POST.json"), "utf8");
// The gate refuses a POST.json over 16384 bytes (post_file), so check the
// size here instead of discovering it at submission time.
const byteSize = Buffer.byteLength(raw, "utf8");
if (byteSize > 16384) {
  throw new Error(`POST.json is ${byteSize} bytes, over the 16384 byte cap`);
}
const post = JSON.parse(raw);
if (
  typeof post !== "object" ||
  post === null ||
  typeof post.url !== "string" ||
  post.url.length === 0
) {
  throw new Error("POST.json must be an object with a non-empty string url");
}

mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "POST.json"), JSON.stringify(post, null, 2) + "\n");
console.log(`POST.json -> ${join(outDir, "POST.json")} (${post.url})`);
