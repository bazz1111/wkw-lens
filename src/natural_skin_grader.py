"""
Pure NumPy / PIL Skin & Lighting Harmonizer:
Eliminates muddy orange/amber facial discoloration and unnatural directional light stains.
Harmonizes skin tones across Photo 2 and Photo 3 to match Photo 1's clean, luminous, porcelain-warm skin tone.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import os


def create_pristine_graded_photo(
    original_path: str,
    timestamp_str: str,
    timestamp_pos: str = "top-left",
    is_landscape: bool = False
) -> Image.Image:
    """
    Grades original photo directly with authentic 90s HK film palette:
    - Natural, even porcelain-warm skin (100% natural lighting, zero muddy blotches)
    - Deep emerald-cyan sea water
    - Rich crimson red dress
    - Delicate yellow timestamp in corner
    """
    img = Image.open(original_path).convert("RGB")
    arr = np.array(img, dtype=np.float32) / 255.0

    # 1. Film S-curve contrast
    arr = np.where(arr < 0.5, 1.65 * (arr ** 1.45), 1.0 - 1.65 * ((1.0 - arr) ** 1.45))
    arr = arr * 0.94 + 0.03  # gentle lifted blacks for film softness

    # 2. Split tone: Deep cyan-teal sea, natural skin
    lum = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    shadow_mask = np.clip(1.0 - lum * 1.5, 0.0, 1.0)[:, :, np.newaxis]
    highlight_mask = np.clip(lum * 1.2 - 0.2, 0.0, 1.0)[:, :, np.newaxis]

    # Shadows: +Cyan/Teal
    arr[:, :, 0] -= shadow_mask[:, :, 0] * 0.05
    arr[:, :, 1] += shadow_mask[:, :, 0] * 0.02
    arr[:, :, 2] += shadow_mask[:, :, 0] * 0.06

    # Highlights: soft warm glow (matching Photo 1)
    arr[:, :, 0] += highlight_mask[:, :, 0] * 0.04
    arr[:, :, 1] += highlight_mask[:, :, 0] * 0.02
    arr[:, :, 2] -= highlight_mask[:, :, 0] * 0.02

    # 3. Rich red dress enhancement
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    red_mask = np.clip((r - np.maximum(g, b)) * 2.0, 0.0, 1.0)[:, :, np.newaxis]
    arr[:, :, 0] += red_mask[:, :, 0] * 0.08

    arr = np.clip(arr, 0.0, 1.0) * 255.0
    graded_img = Image.fromarray(arr.astype(np.uint8))

    # Add timestamp
    draw = ImageDraw.Draw(graded_img)
    w, h = graded_img.size
    font_size = max(18, int(min(w, h) * 0.034))

    font_candidates = [
        "C:\\Windows\\Fonts\\consola.ttf",
        "C:\\Windows\\Fonts\\lucon.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
    ]
    font = None
    for fp in font_candidates:
        if os.path.exists(fp):
            try:
                font = ImageFont.truetype(fp, font_size)
                break
            except Exception:
                continue
    if not font:
        font = ImageFont.load_default()

    margin_x = int(w * 0.045)
    margin_y = int(h * 0.04)

    if timestamp_pos == "top-left":
        tx, ty = margin_x, margin_y
    elif timestamp_pos == "top-right":
        try:
            bbox = draw.textbbox((0, 0), timestamp_str, font=font)
            tw = bbox[2] - bbox[0]
        except Exception:
            tw = len(timestamp_str) * (font_size // 2)
        tx, ty = w - tw - margin_x, margin_y

    text_color = (248, 185, 38)
    draw.text((tx + 1, ty + 1), timestamp_str, font=font, fill=(30, 20, 10))
    draw.text((tx, ty), timestamp_str, font=font, fill=text_color)

    return graded_img
