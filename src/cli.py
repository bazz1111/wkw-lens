"""
Command Line Interface for Wong Kar-wai Lens (wkw-lens)
"""

import argparse
import os
import sys
from PIL import Image
from .pipeline import process_image
from .color_grading import grade_image


def main():
    if sys.stdout and hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    parser = argparse.ArgumentParser(
        description="Wong Kar-wai Lens (wkw-lens): Transform everyday photos into 1990s Hong Kong cinema stills & candid film snapshots."
    )
    parser.add_argument("input", help="Path to input photo/image")
    parser.add_argument("-o", "--output", help="Path to save output image (default: <input>_wkw.jpg)", default=None)
    parser.add_argument(
        "-s", "--style", choices=["wkw", "night", "noir", "romance"], default="wkw",
        help="Color grading style preset: 'wkw' (day/twilight), 'night' (night street/taxis), 'romance' (soft warm) [default: wkw]"
    )
    parser.add_argument(
        "-f", "--frame", choices=["none", "film", "cinema"], default="none",
        help="Frame layout: 'none' (full-bleed snapshot), 'film' (35mm Kodak border), 'cinema' (2.39:1 widescreen) [default: none]"
    )
    parser.add_argument("-t", "--timestamp", default="'97  7 16", help="Vintage yellow digital date stamp (e.g. \"'97 7 16\", \"'95 11 12\", 'none' to disable) [default: '97 7 16]")
    parser.add_argument("--pos", choices=["top-left", "top-right", "bottom-right"], default="top-left", help="Timestamp position [default: top-left]")
    parser.add_argument("-zh", "--chinese", default="", help="Optional Chinese subtitle text")
    parser.add_argument("-en", "--english", default="", help="Optional English subtitle text")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"[!] Error: Input file '{args.input}' not found.")
        return

    out_path = args.output
    if not out_path:
        base, ext = os.path.splitext(args.input)
        out_path = f"{base}_wkw_{args.style}.jpg"

    print(f"[+] Loading photo: {args.input}")
    img = Image.open(args.input)

    print(f"[+] Applying 90s Hong Kong film grading ({args.style.upper()})...")
    # Apply continuous color grading
    graded = grade_image(img, style=args.style)

    # Process frame & subtitles
    result = process_image(
        input_image=graded,
        style=args.style,
        frame_type=args.frame,
        chinese_text=args.chinese,
        english_text=args.english,
        grain_intensity=0.0,
        halation_intensity=0.0,
    )

    # Add timestamp if requested
    if args.timestamp and args.timestamp.lower() != "none":
        from .candid_processor import add_delicate_timestamp
        result = add_delicate_timestamp(result, timestamp_str=args.timestamp, position=args.pos)

    out_dir = os.path.dirname(os.path.abspath(out_path))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    result.save(out_path, quality=98)
    print(f"[+] Successfully saved Hong Kong film photo to: {out_path}!")


if __name__ == "__main__":
    main()
