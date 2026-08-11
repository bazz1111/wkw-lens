"""
Film Effects Engine: Grain, Halation, and Step-printing motion blur
"""

from PIL import Image, ImageFilter
import numpy as np


def add_film_grain(img: Image.Image, intensity: float = 0.025) -> Image.Image:
    """
    Simulates subtle, organic 35mm film silver halide micro-grain (ISO 100/200 fine grain look).
    Weighted on midtones to keep skin and highlights crystal clear.
    """
    arr = np.array(img, dtype=np.float32)
    h, w, c = arr.shape

    # Midtone mask: grain is concentrated in midtones, almost invisible in pure highlights/shadows
    lum = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]) / 255.0
    midtone_weight = np.clip(1.0 - 3.5 * ((lum - 0.5) ** 2), 0.15, 1.0)[:, :, np.newaxis]

    # Organic micro noise
    noise = np.random.normal(0.0, 255.0 * intensity, (h, w, 1)) * midtone_weight

    arr = arr + noise
    arr = np.clip(arr, 0.0, 255.0).astype(np.uint8)
    return Image.fromarray(arr)


def add_halation(img: Image.Image, radius: int = 8, intensity: float = 0.35) -> Image.Image:
    """
    Simulates Kodak film halation (red-orange glow around strong highlights).
    """
    arr = np.array(img, dtype=np.float32)

    # Extract highlights based on luminance
    luminance = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    highlight_mask = np.clip((luminance - 180.0) / 75.0, 0.0, 1.0)

    # Create red-tinted glow image
    glow_arr = np.zeros_like(arr)
    glow_arr[:, :, 0] = highlight_mask * 255.0  # Red channel strong
    glow_arr[:, :, 1] = highlight_mask * 120.0  # Green channel warm
    glow_arr[:, :, 2] = highlight_mask * 40.0   # Blue channel minimal

    glow_img = Image.fromarray(glow_arr.astype(np.uint8))
    blurred_glow = glow_img.filter(ImageFilter.GaussianBlur(radius=radius))
    blurred_glow_arr = np.array(blurred_glow, dtype=np.float32)

    # Additive blend
    arr = arr + blurred_glow_arr * intensity
    arr = np.clip(arr, 0.0, 255.0).astype(np.uint8)
    return Image.fromarray(arr)


def add_motion_blur_simulation(img: Image.Image, radius: int = 4, angle: float = 0.0) -> Image.Image:
    """
    Simulates Christopher Doyle style subtle step-printing motion drag.
    """
    blurred = img.filter(ImageFilter.GaussianBlur(radius=radius))
    return Image.blend(img, blurred, alpha=0.25)
