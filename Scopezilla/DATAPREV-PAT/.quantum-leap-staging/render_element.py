#!/usr/bin/env python3
"""Screenshot a single element of an HTML file to PNG at 2x device scale.
Element screenshot captures the element's full rendered size (no viewport clip),
so wide content is never cropped and text never overlaps a fixed frame.

Usage: render_element.py <page.html> <css-selector> <out.png>
"""
import sys, pathlib
from playwright.sync_api import sync_playwright

def main():
    page_path = pathlib.Path(sys.argv[1]).resolve()
    selector = sys.argv[2]
    out = pathlib.Path(sys.argv[3])
    out.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 2040, "height": 1400}, device_scale_factor=2)
        page.goto(page_path.as_uri())
        page.wait_for_load_state("networkidle")
        el = page.query_selector(selector)
        box = el.bounding_box()
        print(f"element {selector}: {box['width']:.0f}x{box['height']:.0f} css px -> {box['width']*2:.0f}x{box['height']*2:.0f} px @2x")
        el.screenshot(path=str(out))
        print(f"wrote {out}")
        browser.close()

if __name__ == "__main__":
    main()
