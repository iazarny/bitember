"""
Placeholder for future diff viewer settings.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class DiffViewerSettings:
    """Settings for diff viewer behavior and appearance."""
    
    # Appearance
    font_family: str = "Menlo, Consolas, 'Courier New', monospace"
    font_size: int = 12
    theme: str = "dark"  # 'dark' or 'light'
    show_line_numbers: bool = True
    show_minimap: bool = True
    show_bezier_connections: bool = True
    
    # Behavior
    sync_scrolling: bool = True
    word_wrap: bool = False
    ignore_whitespace: bool = False
    ignore_case: bool = False
    
    # Colors (for future theming)
    color_inserted: str = "#2ECC71"  # green
    color_deleted: str = "#E74C3C"  # red
    color_modified: str = "#4682B4"  # blue
    color_equal: str = "#646469"  # grey
    
    # Minimap
    minimap_width_percent: float = 0.05
    minimap_show_colors: bool = True
    
    # Gutter/Spacer
    gutter_width_percent: float = 0.05
    
    @classmethod
    def load(cls) -> "DiffViewerSettings":
        """Load settings from config file."""
        # TODO: Load from ~/.gitember/diff_settings.json
        return cls()
    
    def save(self) -> None:
        """Save settings to config file."""
        # TODO: Save to ~/.gitember/diff_settings.json
        pass

