"""
True 1990s Hong Kong Cinema & Wong Kar-wai Film Emulsion Engine.

Implements the 4 Core Optical Signatures of Christopher Doyle's Cinematography:
1. Kodak 500T / 2383 Film Matrix (Tungsten emerald-cyan shadows, golden amber highlights, dense ruby red isolation).
2. Optical Halation & Black Pro-Mist Bloom (Soft glow around lights + red fringe bleed into shadows).
3. Analog Emulsion S-Curve (Velvety lifted blacks, soft rolled-off highlights, zero digital harshness).
4. Vintage Lens Vignette & Chromatic Dispersion (Subtle corner falloff).
"""

from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
import numpy as np
import os


def apply_pro_mist_halation(img: Image.Image, intensity: float = 0.45) -> Image.Image:
    """
    Simulates Schneider Black Pro-Mist Filter & Kodak 35mm Red Halation:
    - Extracts highlights (lights, neon, bright reflections)
    - Blurs with wide radius
    - Tints with warm red/amber halation color
    - Blends smoothly to remove digital sharpness
    """
    arr = np.array(img.convert("RGB"), dtype=np.float32) / 255.0
    lum = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]

    # Extract high-luminance light sources
    highlight_thresh = 0.62
    highlight_mask = np.clip((lum - highlight_thresh) / (1.0 - highlight_thresh + 1e-5), 0.0, 1.0)
    
    # Create Halation Glow Layer (Red-Orange tinted light bleed)
    glow_r = arr[:, :, 0] * highlight_mask * 1.3
    glow_g = arr[:, :, 1] * highlight_mask * 0.75
    glow_b = arr[:, :, 2] * highlight_mask * 0.35
    
    glow_arr = np.stack([glow_r, glow_g, glow_b], axis=2)
    glow_arr = np.clip(glow_arr * 255.0, 0, 255).astype(np.uint8)
    glow_img = Image.fromarray(glow_arr)

    # Multi-pass optical diffusion (Pro-Mist 1/2 Bloom)
    bloom_large = glow_img.filter(ImageFilter.GaussianBlur(radius=18))
    bloom_tight = glow_img.filter(ImageFilter.GaussianBlur(radius=6))

    # Blend back onto image using Screen mode
    base_arr = arr * 255.0
    b_l_arr = np.array(bloom_large, dtype=np.float32) * intensity
    b_t_arr = np.array(bloom_tight, dtype=np.float32) * (intensity * 0.8)
    
    # Screen blend: 1 - (1 - a)(1 - b)
    blended = 255.0 - (255.0 - base_arr) * (255.0 - (b_l_arr + b_t_arr)) / 255.0
    return Image.fromarray(np.clip(blended, 0, 255).astype(np.uint8))


def apply_wkw_kodak_500t_grading(img: Image.Image, preset: str = "classic_wkw") -> Image.Image:
    """
    Emulates Kodak Vision3 500T & Kodak 2383 Print Stock:
    - Shadows: Deep turquoise / emerald cyan (孔雀青绿)
    - Midtones: Warm vintage film density
    - Highlights: Golden tungsten amber (暖金琥珀)
    - Reds: Deep crimson red isolation (浓郁正红)
    """
    arr = np.array(img.convert("RGB"), dtype=np.float32) / 255.0

    # 1. Analog Film Tone Curve (Soft toe lift + compressed highlight shoulder)
    # Smooth Hermite film curve
    arr = 3.0 * (arr ** 2) - 2.0 * (arr ** 3)  # Smooth S-curve
    arr = arr * 0.92 + 0.035  # Lift deep black to smoky analog velvet

    # 2. Luminance-based split toning (Christopher Doyle palette)
    lum = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    shadows = np.clip(1.0 - lum * 1.8, 0.0, 1.0)
    highlights = np.clip(lum * 1.5 - 0.4, 0.0, 1.0)

    if preset in ["classic_wkw", "kennedy_town", "street_corner"]:
        # Classic Fallen Angels / Chungking Express (Teal & Amber)
        arr[:, :, 0] -= shadows * 0.08  # Cyan shadows (-Red)
        arr[:, :, 1] += shadows * 0.03  # Emerald shadows (+Green)
        arr[:, :, 2] += shadows * 0.09  # Deep blue shadows (+Blue)

        arr[:, :, 0] += highlights * 0.07  # Amber highlights (+Red)
        arr[:, :, 1] += highlights * 0.04  # Golden highlights (+Green)
        arr[:, :, 2] -= highlights * 0.05  # Warm highlights (-Blue)

    elif preset in ["night_noir", "taxi", "sushi"]:
        # Night Noir / Neon (Deep Peacock Green & Tungsten Neon)
        arr[:, :, 0] -= shadows * 0.09
        arr[:, :, 1] += shadows * 0.04
        arr[:, :, 2] += shadows * 0.10

        arr[:, :, 0] += highlights * 0.09
        arr[:, :, 1] += highlights * 0.05
        arr[:, :, 2] -= highlights * 0.06

    elif preset in ["golden_hour", "sunset"]:
        # Happy Together / 2046 Sunset (Intense warm amber & burnt orange)
        arr[:, :, 0] += shadows * 0.03
        arr[:, :, 1] += shadows * 0.01
        arr[:, :, 2] += shadows * 0.04

        arr[:, :, 0] += highlights * 0.12
        arr[:, :, 1] += highlights * 0.06
        arr[:, :, 2] -= highlights * 0.08

    elif preset in ["melancholy_cool", "skyscraper", "snow"]:
        # Ashes of Time / Chungking Melancholy (Moody desaturated cyan-grey)
        arr[:, :, 0] -= shadows * 0.07
        arr[:, :, 1] += shadows * 0.02
        arr[:, :, 2] += shadows * 0.08

    # 3. Dense Crimson Red Isolation (Enhance reds into deep film velvet)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    red_dominance = np.clip((r - np.maximum(g, b)) * 2.5, 0.0, 1.0)
    arr[:, :, 0] += red_dominance * 0.10
    arr[:, :, 1] -= red_dominance * 0.03
    arr[:, :, 2] -= red_dominance * 0.03

    arr = np.clip(arr * 255.0, 0, 255).astype(np.uint8)
    return Image.fromarray(arr)


def apply_vintage_lens_vignette(img: Image.Image, strength: float = 0.28) -> Image.Image:
    """
    Applies subtle optical corner falloff from vintage prime lenses.
    """
    w, h = img.size
    x = np.linspace(-1, 1, w)
    y = np.linspace(-1, 1, h)
    xx, yy = np.meshgrid(x, y)
    radius = np.sqrt(xx ** 2 + yy ** 2)
    
    # Vignette mask
    vignette = np.clip(1.0 - (radius - 0.45) * strength, 0.72, 1.0)[:, :, np.newaxis]
    
    arr = np.array(img, dtype=np.float32) * vignette
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def transform_to_wkw_masterpiece(
    input_path: str,
    output_path: str,
    preset: str = "classic_wkw",
    timestamp: str = "'95 11 12",
    timestamp_pos: str = "top-left"
):
    """
    End-to-End Master Cinema Transformation Pipeline.
    """
    img = Image.open(input_path).convert("RGB")
    
    # 1. Pro-Mist Halation & Optical Bloom
    bloomed = apply_pro_mist_halation(img, intensity=0.42)
    
    # 2. Kodak 500T / 2383 Color Grade
    graded = apply_wkw_kodak_500t_grading(bloomed, preset=preset)
    
    # 3. Vintage Lens Vignette
    vignetted = apply_vintage_lens_vignette(graded, strength=0.25)
    
    # 4. Delicate LCD Yellow Timestamp
    from src.candid_processor import add_delicate_timestamp
    final = add_delicate_timestamp(vignetted, timestamp_str=timestamp, position=timestamp_pos)
    
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    final.save(output_path, quality=98)
    return final
