"""
Refined Film Grain Engine:
Applies ultra-subtle, organic ISO 100/200 fine 35mm silver halide grain.
Midtone-weighted (grain lives in midtones, clear in shadows/highlights), zero chromatic noise.
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os


def apply_candid_hk_grading(img: Image.Image) -> Image.Image:
    """
    Applies authentic, soft 90s Hong Kong film color:
    - Warm skin tones, muted cyan/teal water shadows
    - Clean, natural contrast
    """
    arr = np.array(img.convert("RGB"), dtype=np.float32) / 255.0

    # Gentle film gamma curve
    arr = arr ** 0.95

    # Split-tone: Muted cyan/green shadows, warm golden skin tones
    lum = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    shadow_mask = np.clip(1.0 - lum * 1.5, 0.0, 1.0)[:, :, np.newaxis]
    highlight_mask = np.clip(lum * 1.3 - 0.3, 0.0, 1.0)[:, :, np.newaxis]

    # Shadows: subtle +Cyan/Teal
    arr[:, :, 0] -= shadow_mask[:, :, 0] * 0.03
    arr[:, :, 1] += shadow_mask[:, :, 0] * 0.02
    arr[:, :, 2] += shadow_mask[:, :, 0] * 0.04

    # Highlights: subtle +Warm Gold
    arr[:, :, 0] += highlight_mask[:, :, 0] * 0.04
    arr[:, :, 1] += highlight_mask[:, :, 0] * 0.02
    arr[:, :, 2] -= highlight_mask[:, :, 0] * 0.03

    arr = np.clip(arr, 0.0, 1.0) * 255.0
    return Image.fromarray(arr.astype(np.uint8))


def add_subtle_micro_grain(img: Image.Image, intensity: float = 0.03) -> Image.Image:
    """
    Adds ultra-fine, barely-perceptible 35mm film micro-grain (ISO 100/200 fine grain look).
    Weighted towards midtones, perfectly clean on faces and highlights.
    """
    arr = np.array(img, dtype=np.float32)
    h, w, _ = arr.shape

    # Midtone mask: grain is naturally visible in midtones, almost invisible in pure highlights/shadows
    lum = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]) / 255.0
    # Parabolic curve peaking at 0.5 midtone
    midtone_weight = np.clip(1.0 - 3.5 * ((lum - 0.5) ** 2), 0.15, 1.0)[:, :, np.newaxis]

    # Micro noise: std dev is around 6~8 (out of 255)
    noise = np.random.normal(0.0, 255.0 * intensity, (h, w, 1)) * midtone_weight

    arr = arr + noise
    arr = np.clip(arr, 0.0, 255.0).astype(np.uint8)
    return Image.fromarray(arr)


def add_delicate_timestamp(
    img: Image.Image,
    timestamp_str: str = "'94  5  1",
    position: str = "top-left"
) -> Image.Image:
    """
    Draws a tiny, elegant 1990s digital camera timestamp.
    """
    result = img.copy()
    draw = ImageDraw.Draw(result)
    w, h = result.size

    # Ultra-small, unobtrusive font size (approx 2% of image dimension)
    font_size = max(12, int(min(w, h) * 0.025))

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

    margin_x = int(w * 0.04)
    margin_y = int(h * 0.035)

    if position == "top-left":
        tx, ty = margin_x, margin_y
    elif position == "top-right":
        try:
            bbox = draw.textbbox((0, 0), timestamp_str, font=font)
            tw = bbox[2] - bbox[0]
        except Exception:
            tw = len(timestamp_str) * (font_size // 2)
        tx, ty = w - tw - margin_x, margin_y
    else:  # bottom-right
        try:
            bbox = draw.textbbox((0, 0), timestamp_str, font=font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
        except Exception:
            tw = len(timestamp_str) * (font_size // 2)
            th = font_size
        tx, ty = w - tw - margin_x, h - th - margin_y

    # Retro soft orange-yellow
    text_color = (245, 175, 40)

    # 1px soft shadow for legibility over bright backgrounds
    draw.text((tx + 1, ty + 1), timestamp_str, font=font, fill=(30, 25, 10))
    draw.text((tx, ty), timestamp_str, font=font, fill=text_color)

    return result


def process_clean_snapshot(
    input_path: str,
    output_path: str,
    timestamp: str = "'94  5  1",
    timestamp_pos: str = "top-left",
    grain_intensity: float = 0.025,  # Ultra-fine subtle grain
):
    img = Image.open(input_path)
    graded = apply_candid_hk_grading(img)
    grained = add_subtle_micro_grain(graded, intensity=grain_intensity)
    final = add_delicate_timestamp(grained, timestamp_str=timestamp, position=timestamp_pos)
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    final.save(output_path, quality=98)
    print(f"[+] Saved clean 90s snapshot with micro-grain to: {output_path}")
