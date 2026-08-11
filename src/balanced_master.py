"""
Balanced Master Grading Engine:
Brings back the rich, authentic 1990s Hong Kong cinema flavor (Christopher Doyle palette)
while keeping lighting natural (no harsh overexposure), grain silky-fine (no sand/dirt effect),
and composition clean (small subtle timestamp, no intrusive subtitles/borders).
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import os


def apply_balanced_cinema_grade(img: Image.Image) -> Image.Image:
    """
    Applies authentic 90s Hong Kong Cinema color science:
    - Rich ruby reds & deep emerald-teal shadows (Christopher Doyle's signature)
    - Warm golden hour glow on skin without overexposed blown-out highlights
    - Matte lifted film blacks (Kodak Vision3 emulsion feel)
    - Pro-Mist 1/8 subtle highlight roll-off
    """
    img_rgb = img.convert("RGB")
    arr = np.array(img_rgb, dtype=np.float32) / 255.0

    # 1. Film S-Curve with lifted black toe (prevents crushing, adds cinematic film depth)
    # Shadows slightly lifted, midtones deepened, highlights rolled off smoothly
    arr = np.where(
        arr < 0.5,
        1.85 * (arr ** 1.6),
        1.0 - 1.85 * ((1.0 - arr) ** 1.6)
    )
    arr = arr * 0.90 + 0.05  # Lifted blacks for velvety film look

    # 2. Chromatic Split-Toning (Teal Shadows + Amber Gold Skin/Highlights)
    lum = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    shadow_mask = np.clip(1.0 - lum * 1.5, 0.0, 1.0)[:, :, np.newaxis]
    highlight_mask = np.clip(lum * 1.4 - 0.35, 0.0, 1.0)[:, :, np.newaxis]

    # Deepen ocean teals in shadows
    arr[:, :, 0] -= shadow_mask[:, :, 0] * 0.06  # -Red
    arr[:, :, 1] += shadow_mask[:, :, 0] * 0.03  # +Green
    arr[:, :, 2] += shadow_mask[:, :, 0] * 0.07  # +Blue

    # Warm amber sunlight on highlights/skin
    arr[:, :, 0] += highlight_mask[:, :, 0] * 0.08  # +Red
    arr[:, :, 1] += highlight_mask[:, :, 0] * 0.04  # +Green
    arr[:, :, 2] -= highlight_mask[:, :, 0] * 0.05  # -Blue

    # 3. Enhance Red Dress & Warm Saturation
    # Boost reds and warm tones selectively
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    red_dominance = np.clip((r - (g + b) / 2.0) * 1.8, 0.0, 1.0)[:, :, np.newaxis]
    arr[:, :, 0] += red_dominance[:, :, 0] * 0.06

    arr = np.clip(arr, 0.0, 1.0) * 255.0
    graded_img = Image.fromarray(arr.astype(np.uint8))

    # 4. Subtle Pro-Mist 1/8 Optical Diffusion (Soft, dreamy highlight bloom, NOT overexposed halo)
    blur_layer = graded_img.filter(ImageFilter.GaussianBlur(radius=6))
    graded_img = Image.blend(graded_img, blur_layer, alpha=0.08)

    return graded_img


def add_silky_micro_texture(img: Image.Image, intensity: float = 0.008) -> Image.Image:
    """
    Adds barely-perceptible, silky 35mm film micro-grain.
    Zero pixel noise, zero grit on faces.
    """
    arr = np.array(img, dtype=np.float32)
    h, w, _ = arr.shape

    # Midtone mask: only present in atmospheric midtones
    lum = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]) / 255.0
    midtone_weight = np.clip(1.0 - 4.0 * ((lum - 0.5) ** 2), 0.0, 1.0)[:, :, np.newaxis]

    # Ultra-soft micro noise
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
    Adds a subtle, elegant 90s vintage digital camera timestamp.
    """
    result = img.copy()
    draw = ImageDraw.Draw(result)
    w, h = result.size

    # Small, elegant font size
    font_size = max(13, int(min(w, h) * 0.026))

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

    # Retro soft golden yellow
    text_color = (248, 182, 36)

    # 1px soft shadow for legibility
    draw.text((tx + 1, ty + 1), timestamp_str, font=font, fill=(25, 20, 10))
    draw.text((tx, ty), timestamp_str, font=font, fill=text_color)

    return result


def process_balanced_master(
    input_path: str,
    output_path: str,
    timestamp: str = "'94  5  1",
    timestamp_pos: str = "top-left",
    grain_intensity: float = 0.008,
):
    img = Image.open(input_path)
    graded = apply_balanced_cinema_grade(img)
    textured = add_silky_micro_texture(graded, intensity=grain_intensity)
    final = add_delicate_timestamp(textured, timestamp_str=timestamp, position=timestamp_pos)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    final.save(output_path, quality=98)
    print(f"[+] Saved balanced master to: {output_path}")
