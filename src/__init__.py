"""
Wong Kar-wai Lens (wkw-lens) Package
"""

from .color_grading import grade_image
from .pipeline import process_image

__version__ = "0.1.0"
__all__ = ["grade_image", "process_image"]
