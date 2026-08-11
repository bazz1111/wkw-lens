"""
Subtitle Engine for 1990s Hong Kong Cinema
Renders classic yellow/white subtitles with black stroke and English translations.
"""

from PIL import Image, ImageDraw, ImageFont
import os


def get_default_font(size: int):
    """
    Attempts to load a standard Chinese/English font on Windows/Linux/macOS, falls back to default.
    """
    font_candidates = [
        # Windows
        "C:\\Windows\\Fonts\\msyhbd.ttc",  # Microsoft YaHei Bold
        "C:\\Windows\\Fonts\\msyh.ttc",    # Microsoft YaHei
        "C:\\Windows\\Fonts\\simsun.ttc",  # SimSun
        "C:\\Windows\\Fonts\\simhei.ttf",  # SimHei
        "C:\\Windows\\Fonts\\arial.ttf",
        # Linux / macOS
        "/System/Library/Fonts/PingFang.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    for font_path in font_candidates:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def render_subtitles(
    img: Image.Image,
    chinese_text: str = "",
    english_text: str = "",
    color: tuple = (246, 211, 45),  # Classic HK Cinema Yellow
    bottom_margin_ratio: float = 0.08,
) -> Image.Image:
    """
    Draws classic Hong Kong cinema bilingual subtitles on the image.
    """
    if not chinese_text and not english_text:
        return img

    result = img.copy()
    draw = ImageDraw.Draw(result)
    w, h = result.size

    # Calculate font sizes relative to image height
    zh_font_size = max(18, int(h * 0.038))
    en_font_size = max(12, int(h * 0.022))

    zh_font = get_default_font(zh_font_size)
    en_font = get_default_font(en_font_size)

    stroke_w = max(2, int(zh_font_size * 0.08))
    stroke_color = (0, 0, 0)

    # Position calculations
    base_y = h - int(h * bottom_margin_ratio)

    if english_text and chinese_text:
        zh_y = base_y - zh_font_size - en_font_size - 8
        en_y = base_y - en_font_size
    elif chinese_text:
        zh_y = base_y - zh_font_size
        en_y = base_y
    else:
        zh_y = base_y
        en_y = base_y - en_font_size

    # Draw Chinese text (Centered with black outline)
    if chinese_text:
        try:
            bbox = draw.textbbox((0, 0), chinese_text, font=zh_font)
            text_w = bbox[2] - bbox[0]
        except Exception:
            text_w = len(chinese_text) * zh_font_size
        zh_x = (w - text_w) // 2

        # Draw stroke outline
        for dx in range(-stroke_w, stroke_w + 1):
            for dy in range(-stroke_w, stroke_w + 1):
                if dx * dx + dy * dy <= stroke_w * stroke_w:
                    draw.text((zh_x + dx, zh_y + dy), chinese_text, font=zh_font, fill=stroke_color)
        draw.text((zh_x, zh_y), chinese_text, font=zh_font, fill=color)

    # Draw English text (Centered with black outline)
    if english_text:
        en_text_upper = english_text.upper()
        try:
            bbox = draw.textbbox((0, 0), en_text_upper, font=en_font)
            text_w = bbox[2] - bbox[0]
        except Exception:
            text_w = len(en_text_upper) * (en_font_size // 2)
        en_x = (w - text_w) // 2

        en_stroke_w = max(1, stroke_w - 1)
        for dx in range(-en_stroke_w, en_stroke_w + 1):
            for dy in range(-en_stroke_w, en_stroke_w + 1):
                if dx * dx + dy * dy <= en_stroke_w * en_stroke_w:
                    draw.text((en_x + dx, en_y + dy), en_text_upper, font=en_font, fill=stroke_color)
        draw.text((en_x, en_y), en_text_upper, font=en_font, fill=(240, 240, 240))

    return result
