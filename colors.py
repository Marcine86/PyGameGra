# Tetris Game Colors **AI**

# UI Colors
BACKGROUND = (0, 0, 30)          # Dark blue background
GRID_LINE = (205, 205, 205)      # Light gray grid lines
TEXT = (255, 255, 255)           # White text
BORDER = (100, 100, 100)         # Dark gray border

# Tetris Block Colors (Standard)
CYAN = (0, 240, 240)             # I-block (Light blue)
BLUE = (0, 0, 240)               # J-block (Blue)
ORANGE = (255, 160, 0)           # L-block (Orange)
YELLOW = (255, 255, 0)           # O-block (Yellow)
GREEN = (0, 240, 0)              # S-block (Green)
PURPLE = (160, 0, 240)           # T-block (Purple)
RED = (240, 0, 0)                # Z-block (Red)

# Block color mapping by ID
BLOCK_COLORS = {
    0: CYAN,
    1: BLUE,
    2: ORANGE,
    3: YELLOW,
    4: GREEN,
    5: PURPLE,
    6: RED,
}

# Additional Colors
EMPTY = (0, 0, 0)                # Empty cell
GHOST = (100, 100, 100)          # Ghost piece (preview)
FILLED = (200, 200, 200)         # Empty grid cell fill
