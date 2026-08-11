"""
Main Processing Pipeline for Wong Kar-wai Lens
"""

from PIL import Image
from .color_grading import grade_image
from .film_effects import add_film_grain, add_halation, add_motion_blur_simulation
from .frame_renderer import render_cinemascope_frame, render_35mm_film_border
from .subtitle_engine import render_subtitles


def process_image(
    input_image: Image.Image,
    style: str = "wkw",
    frame_type: str = "cinema",  # "cinema", "film", "none"
    chinese_text: str = "",
    english_text: str = "",
    grain_intensity: float = 0.12,
    halation_intensity: float = 0.25,
    blur_intensity: float = 0.0,
) -> Image.Image:
    """
    Complete end-to-end pipeline:
    1. Color Grading (Teal & Amber / Johnnie To / Romance)
    2. Optical Halation & Film Grain
    3. Frame Padding (CinemaScope 2.39:1 / 35mm Film Roll Border)
    4. Subtitle Overlay
    """
    # 1. Color Grading
    graded = grade_image(input_image, style=style)

    # 2. Film Effects
    if halation_intensity > 0:
        graded = add_halation(graded, intensity=halation_intensity)
    if blur_intensity > 0:
        graded = add_motion_blur_simulation(graded, radius=int(blur_intensity * 8))
    if grain_intensity > 0:
        graded = add_film_grain(graded, intensity=grain_intensity)

    # 3. Frame Rendering
    if frame_type == "cinema":
        framed, _, _ = render_cinemascope_frame(graded, target_ratio=2.39)
    elif frame_type == "film":
        framed = render_35mm_film_border(graded)
    else:
        framed = graded

    # 4. Subtitles
    if chinese_text or english_text:
        framed = render_subtitles(framed, chinese_text=chinese_text, english_text=english_text)

    return framed
