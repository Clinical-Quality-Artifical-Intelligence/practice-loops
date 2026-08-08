#!/usr/bin/env python3
"""Build a distributable .docx from a Markdown article using Pandoc.

Replaces two hand-rolled OOXML generators (build_linkedin_article_docx.js and .py,
~25 KB of ZIP-writing and CRC-32) that held the article text as string arrays inside
the code. They had drifted apart, wrote to the same output path so whichever ran last
won, and neither could render a table at all.

The article is now Markdown, so the prose is reviewable in a diff and the build is a
single deterministic step.

Usage:
    python scripts/build_article.py                      # build the default article
    python scripts/build_article.py path/to/article.md    # build a specific one
    python scripts/build_article.py --list                # show what is available

Requires Pandoc on PATH: winget install --id JohnMacFarlane.Pandoc --scope user
"""
import shutil
import subprocess
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOG = ROOT / "docs" / "blog"
DEFAULT = BLOG / "2026-08-08-beyond-vibe-coding.md"
OUT_DIR = ROOT / "dist" / "articles"

# A reference .docx supplies house styles (fonts, heading colours, spacing). Optional:
# create one with `pandoc -o reference.docx --print-default-data-file reference.docx`,
# restyle it in Word, and drop it here.
REFERENCE = BLOG / "reference.docx"


def die(msg, code=1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def main(argv):
    if "--list" in argv:
        if not BLOG.exists():
            die(f"no blog directory at {BLOG}")
        for md in sorted(BLOG.glob("*.md")):
            print(md.relative_to(ROOT).as_posix())
        return 0

    pandoc = shutil.which("pandoc")
    if not pandoc:
        die("pandoc not found on PATH. Install it with:\n"
            "  winget install --id JohnMacFarlane.Pandoc --scope user\n"
            "then open a new shell so PATH is picked up.")

    src = pathlib.Path(argv[0]).resolve() if argv else DEFAULT
    if not src.exists():
        die(f"no such article: {src}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / (src.stem + ".docx")

    # Word holds an exclusive lock on an open .docx, and pandoc reports that as a
    # Haskell backtrace ending in "withBinaryFile: permission denied", which does not
    # tell the reader to close the document. Check first and say so plainly.
    if out.exists():
        try:
            out.open("ab").close()
        except PermissionError:
            die(f"cannot write {out.name} — it is open in another program.\n"
                f"  Close it in Word (or whatever has it open) and run again.\n"
                f"  Full path: {out}")

    # yaml_metadata_block makes the YAML front matter become the document title
    # block instead of being rendered as body text; smart gives proper quotes and
    # dashes. --standalone is what emits the title block at all.
    cmd = [
        pandoc, str(src),
        "-o", str(out),
        "--from", "markdown+yaml_metadata_block+smart",
        "--standalone",
    ]

    if REFERENCE.exists():
        cmd += ["--reference-doc", str(REFERENCE)]
        print(f"using house styles from {REFERENCE.relative_to(ROOT).as_posix()}")

    print("+ " + " ".join(cmd[1:]))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        die(f"pandoc exited {result.returncode}", result.returncode)

    size = out.stat().st_size
    print(f"\nbuilt {out.relative_to(ROOT).as_posix()} ({size:,} bytes)")
    print("dist/ is gitignored — the Markdown source is the artefact of record.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
