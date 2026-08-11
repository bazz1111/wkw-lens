"""
Frame & Aspect Ratio Rendering Engine
Supports 2.39:1 CinemaScope, 35mm Kodak film roll borders, and 4:3 vintage frames.
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np


def render_cinemascope_frame(img: Image.Image, target_ratio: float = 2.39) -> tuple[Image.Image, int, int]:
    """
    Pads image with top and bottom cinema black bars to achieve target 2.39:1 CinemaScope ratio.
    Returns: (framed_image, content_top_y, content_bottom_y)
    """
    w, h = img.size
    current_ratio = w / h

    if current_ratio >= target_ratio:
        # Already wide enough, pad top/bottom slightly for aesthetics
        pad_h = int(h * 0.1)
        new_h = h + pad_h * 2
        framed = Image.new("RGB", (w, new_h), (0, 0, 0))
        framed.paste(img, (0, pad_h))
        return framed, pad_h, pad_h + h
    else:
        # Vertical or standard ratio: Add top and bottom letterbox bars
        new_h = int(w / target_ratio)
        if new_h < h:
            # If target height is smaller, we expand canvas height to fit original image with bars
            bar_height = int(w * 0.12)
            new_h = h + bar_height * 2
            framed = Image.new("RGB", (w, new_h), (0, 0, 0))
            framed.paste(img, (0, bar_height))
            return framed, bar_height, bar_height + h
        else:
            bar_height = (new_h - h) // 2
            framed = Image.new("RGB", (w, new_h), (0, 0, 0))
            framed.paste(img, (0, bar_height))
            return framed, bar_height, bar_height + h


def render_35mm_film_border(img: Image.Image) -> Image.Image:
    """
    Adds authentic 35mm Kodak Ektachrome film roll borders with sprocket holes and film stamps.
    """
    w, h = img.size
    is_landscape = w > h

    if is_landscape:
        # Sprockets on Top and Bottom
        border_size = int(h * 0.14)
        new_w = w
        new_h = h + border_size * 2
        canvas = Image.new("RGB", (new_w, new_h), (8, 8, 8))
        canvas.paste(img, (0, border_size))
        draw = ImageDraw.Draw(canvas)

        # Draw sprocket holes along top and bottom borders
        sprocket_w = int(border_size * 0.45)
        sprocket_h = int(border_size * 0.35)
        sprocket_spacing = int(sprocket_w * 1.6)

        num_sprockets = new_w // sprocket_spacing
        start_x = (new_w - (num_sprockets * sprocket_spacing)) // 2

        sprocket_color = (2, 2, 2)
        sprocket_outline = (25, 25, 25)

        for i in range(num_sprockets + 1):
            sx = start_x + i * sprocket_spacing

            # Top sprocket
            sy_top = border_size // 2 - sprocket_h // 2
            draw.rounded_rectangle(
                [sx, sy_top, sx + sprocket_w, sy_top + sprocket_h],
                radius=4,
                fill=sprocket_color,
                outline=sprocket_outline,
            )

            # Bottom sprocket
            sy_bot = new_h - border_size // 2 - sprocket_h // 2
            draw.rounded_rectangle(
                [sx, sy_bot, sx + sprocket_w, sy_bot + sprocket_h],
                radius=4,
                fill=sprocket_color,
                outline=sprocket_outline,
            )

        # Draw Film Text (Gold / Orange vintage print)
        gold_color = (235, 175, 55)
        try:
            # Default text rendering
            draw.text((int(new_w * 0.12), int(border_size * 0.15)), "KODAK EKTACHROME 100D", fill=gold_color)
            draw.text((int(new_w * 0.65), int(border_size * 0.15)), "14A", fill=gold_color)
            draw.text((int(new_w * 0.82), int(border_size * 0.15)), "WKW CINEMA", fill=gold_color)

            draw.text((int(new_w * 0.15), new_h - int(border_size * 0.3)), "35MM FILM", fill=gold_color)
            draw.text((int(new_w * 0.50), new_h - int(border_size * 0.3)), "▶ 14", fill=gold_color)
            draw.text((int(new_w * 0.85), new_h - int(border_size * 0.3)), "24", fill=gold_color)
        except Exception:
            pass

        return canvas
    else:
        # Vertical Portrait: Sprockets on Left and Right borders
        border_size = int(w * 0.13)
        new_w = w + border_size * 2
        new_h = h
        canvas = Image.new("RGB", (new_w, new_h), (8, 8, 8))
        canvas.paste(img, (border_size, 0))
        draw = ImageDraw.Draw(canvas)

        sprocket_w = int(border_size * 0.38)
        sprocket_h = int(border_size * 0.5)
        sprocket_spacing = int(sprocket_h * 1.6)

        num_sprockets = new_h // sprocket_spacing
        start_y = (new_h - (num_sprockets * sprocket_spacing)) // 2

        sprocket_color = (2, 2, 2)
        sprocket_outline = (25, 25, 25)

        for i in range(num_sprockets + 1):
            sy = start_y + i * sprocket_spacing

            # Left sprocket
            sx_left = border_size // 2 - sprocket_w // 2
            draw.rounded_rectangle(
                [sx_left, sy, sx_left + sprocket_w, sy + sprocket_h],
                radius=4,
                fill=sprocket_color,
                outline=sprocket_outline,
            )

            # Right sprocket
            sx_right = new_w - border_size // 2 - sprocket_w // 2
            draw.rounded_rectangle(
                [sx_right, sy, sx_right + sprocket_w, sy + sprocket_h],
                radius=4,
                fill=sprocket_color,
                outline=sprocket_outline,
            )

        gold_color = (235, 175, 55)
        try:
            draw.text((int(border_size * 0.15), int(new_h * 0.15)), "KODAK", fill=gold_color)
            draw.text((int(border_size * 0.15), int(new_h * 0.50)), "35MM", fill=gold_color)
            draw.text((new_w - int(border_size * 0.85), int(new_h * 0.20)), "14A", fill=gold_color)
            draw.text((new_w - int(border_size * 0.85), int(new_h * 0.70)), "WKW", fill=gold_color)
        except Exception:
            pass

        return canvas
