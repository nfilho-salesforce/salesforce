#!/usr/bin/env python3
"""Render each slide of presentation-deck.html to a PNG at the deck's native
1280x720 (at 2x device scale for crispness), driving the deck's own show(k) JS
so each slide is captured exactly as it renders in the browser — full visual
fidelity, no CSS re-implementation.

Usage: render_slides.py <deck.html> <out-png-dir>
"""
import sys, pathlib, time
from playwright.sync_api import sync_playwright

def main():
    deck = pathlib.Path(sys.argv[1]).resolve()
    out_dir = pathlib.Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={"width": 1280, "height": 720}, device_scale_factor=2
        )
        page.goto(deck.as_uri())
        page.wait_for_load_state("networkidle")
        # Hide on-screen chrome (nav bar + slide-number) so the PPTX is clean.
        page.add_style_tag(content=".nav,.slide-num{display:none !important}")
        # Force scale=1 (native) regardless of window fit math, and count slides.
        n = page.evaluate("() => document.querySelectorAll('.slide').length")
        page.evaluate("() => document.documentElement.style.setProperty('--scale', 1)")
        print(f"slides: {n}")
        for k in range(n):
            page.evaluate(f"() => show({k})")
            page.evaluate("() => document.documentElement.style.setProperty('--scale', 1)")
            time.sleep(0.25)  # let the active-slide swap paint
            fp = out_dir / f"slide-{k+1:02d}.png"
            page.screenshot(path=str(fp), clip={"x": 0, "y": 0, "width": 1280, "height": 720})
            print(f"  captured {fp.name}")
        browser.close()

if __name__ == "__main__":
    main()
