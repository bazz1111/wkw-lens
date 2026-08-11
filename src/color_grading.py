"""
Master Hong Kong Cinema & Wong Kar-wai Color Grading Engine.
Integrates Kodak Vision 500T/2383 Film Emulsion, Pro-Mist Bloom, and Halation.
"""

from PIL import Image
from .film_emulation_engine import (
    apply_pro_mist_halation,
    apply_wkw_kodak_500t_grading,
    apply_vintage_lens_vignette,
)


def grade_image(img: Image.Image, style: str = "wkw", intensity: float = 1.0) -> Image.Image:
    """
    Main entry point for true cinematic Wong Kar-wai grading.
    """
    style_lower = style.lower()
    
    # 1. Pro-Mist Halation & Optical Bloom
    bloom_strength = 0.42 * intensity
    bloomed = apply_pro_mist_halation(img, intensity=bloom_strength)

    # 2. Kodak 500T Film Matrix
    preset_map = {
        "wkw": "classic_wkw",
        "night": "night_noir",
        "taxi": "night_noir",
        "noir": "night_noir",
        "romance": "golden_hour",
        "sunset": "golden_hour",
        "snow": "melancholy_cool",
    }
    preset = preset_map.get(style_lower, "classic_wkw")
    graded = apply_wkw_kodak_500t_grading(bloomed, preset=preset)

    # 3. Vintage Lens Vignette
    vignette_strength = 0.22 * intensity
    final = apply_vintage_lens_vignette(graded, strength=vignette_strength)

    return final
