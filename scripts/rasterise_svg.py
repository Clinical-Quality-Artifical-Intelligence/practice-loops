#!/usr/bin/env python3
"""Rasterise an SVG to PNG using headless Edge or Chrome.

SVG is the source format for this project's figures: labels stay diffable, so a wrong
claim cannot get baked into pixels. But some publishing targets (LinkedIn among them)
will not accept SVG upload, so a raster copy is needed at publish time.

Pandoc's own SVG support needs `rsvg-convert`, which is not in winget. Rather than add
a large dependency, this uses the browser already present on every Windows machine.

Output goes to dist/ (gitignored): PNGs are derived artefacts, the SVG is the original.

Usage:
    python scripts/rasterise_svg.py docs/framework/demo-guardrail-check.svg
    python scripts/rasterise_svg.py --all
    python scripts/rasterise_svg.py --all --scale 3
"""
import argparse
import pathlib
import re
import shutil
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "dist" / "figures"

BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

VIEWBOX = re.compile(r'viewBox\s*=\s*"([\d.\s-]+)"')


def find_browser():
    for p in BROWSERS:
        if pathlib.Path(p).exists():
            return p
    for name in ("msedge", "chrome", "chromium"):
        found = shutil.which(name)
        if found:
            return found
    return None


def svg_size(svg_text):
    """Return (width, height) from the viewBox so the viewport matches the artwork.

    Without this the screenshot carries whatever padding the default window size
    leaves around the image.
    """
    m = VIEWBOX.search(svg_text)
    if not m:
        return None
    parts = [float(x) for x in m.group(1).split()]
    if len(parts) != 4:
        return None
    return int(round(parts[2])), int(round(parts[3]))


def rasterise(browser, svg_path, scale):
    svg_text = svg_path.read_text(encoding="utf-8")
    size = svg_size(svg_text)
    if not size:
        print(f"skip {svg_path.name}: no usable viewBox")
        return None
    w, h = size

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    png = OUT_DIR / (svg_path.stem + ".png")
    if png.exists():
        png.unlink()

    # Wrap in a zero-margin page so the SVG fills the viewport exactly.
    html = OUT_DIR / (svg_path.stem + ".tmp.html")
    html.write_text(
        "<!doctype html><meta charset='utf-8'>"
        "<style>html,body{margin:0;padding:0;overflow:hidden}"
        f"svg{{display:block;width:{w}px;height:{h}px}}</style>"
        + svg_text,
        encoding="utf-8",
    )

    uri = "file:///" + str(html).replace("\\", "/")
    cmd = [
        browser, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        f"--force-device-scale-factor={scale}",
        f"--window-size={w},{h}",
        f"--screenshot={png}",
        uri,
    ]
    subprocess.run(cmd, capture_output=True)

    # The browser writes the file after the process returns, so poll rather than
    # assuming it is there.
    for _ in range(60):
        if png.exists() and png.stat().st_size > 0:
            break
        time.sleep(0.25)

    html.unlink(missing_ok=True)

    if not png.exists():
        print(f"FAIL {svg_path.name}: no PNG produced")
        return None
    print(f"ok   {png.relative_to(ROOT).as_posix()} "
          f"({w}x{h} @{scale}x, {png.stat().st_size:,} bytes)")
    return png


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("svg", nargs="*", help="SVG paths to rasterise")
    ap.add_argument("--all", action="store_true",
                    help="rasterise every SVG under docs/framework/")
    ap.add_argument("--scale", type=int, default=2,
                    help="device scale factor, default 2 for high-DPI output")
    args = ap.parse_args()

    browser = find_browser()
    if not browser:
        print("error: no Edge or Chrome found. Install one, or use rsvg-convert "
              "/ Inkscape instead.", file=sys.stderr)
        return 1
    print(f"using {browser}\n")

    if args.all:
        targets = sorted((ROOT / "docs" / "framework").glob("*.svg"))
    else:
        targets = [pathlib.Path(s) for s in args.svg]
    if not targets:
        print("nothing to do — pass SVG paths or --all", file=sys.stderr)
        return 1

    failed = 0
    for t in targets:
        if not t.exists():
            print(f"FAIL {t}: not found")
            failed += 1
            continue
        if rasterise(browser, t.resolve(), args.scale) is None:
            failed += 1

    print(f"\n{len(targets) - failed} of {len(targets)} rasterised")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
