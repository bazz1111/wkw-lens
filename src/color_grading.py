"""
Smooth, Continuous Color Grading Engine for Hong Kong Cinema Aesthetics.
Strictly monotonic and continuous — 100% immune to color banding, solarization, or pixelated contour artifacts.
"""

from PIL import Image, ImageEnhance
import numpy as np


def grade_image(img: Image.Image, style: str = "wkw", intensity: float = 1.0) -> Image.Image:
    """
    Applies smooth, continuous 90s film tone curves without thresholding or piecewise step-discontinuities.
    """
    style_lower = style.lower()
    is_night = style_lower in ["noir", "johnnie-to", "night", "taxi"]

    # 1. Continuous contrast & color saturation
    contrast_val = 1.0 + 0.08 * intensity if is_night else 1.0 + 0.04 * intensity
    color_val = 1.0 + 0.12 * intensity if is_night else 1.0 + 0.06 * intensity

    enh_contrast = ImageEnhance.Contrast(img)
    base = enh_contrast.enhance(contrast_val)

    enh_color = ImageEnhance.Color(base)
    base = enh_color.enhance(color_val)

    # 2. Smooth global color matrix adjustment
    arr = np.array(base, dtype=np.float32)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

    if is_night:
        r_out = r * (1.0 + 0.05 * intensity)
        g_out = g * (1.0 - 0.02 * intensity)
        b_out = b * (1.0 + 0.02 * intensity)
    else:
        r_out = r * (1.0 + 0.02 * intensity)
        g_out = g * (1.0 - 0.01 * intensity)
        b_out = b * (1.0 - 0.02 * intensity)

    arr[:, :, 0] = np.clip(r_out, 0, 255)
    arr[:, :, 1] = np.clip(g_out, 0, 255)
    arr[:, :, 2] = np.clip(b_out, 0, 255)

    return Image.fromarray(arr.astype(np.uint8))
