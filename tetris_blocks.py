from position import Position
from blocks import Block

# Autowygenerowane klasy kształtów z gry Tetris **AI** 
class I_Block(Block):
    """I-Block (Cyan) - 4 tiles in a line"""
    def __init__(self):
        super().__init__(0)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(2, 0), Position(3, 0)],  # Vertical
            1: [Position(0, 0), Position(0, 1), Position(0, 2), Position(0, 3)],  # Horizontal
            2: [Position(0, 0), Position(1, 0), Position(2, 0), Position(3, 0)],  # Vertical
            3: [Position(0, 0), Position(0, 1), Position(0, 2), Position(0, 3)],  # Horizontal
        }


class O_Block(Block):
    """O-Block (Yellow) - 2x2 Square"""
    def __init__(self):
        super().__init__(1)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            1: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            2: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            3: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
        }


class T_Block(Block):
    """T-Block (Purple) - T Shape"""
    def __init__(self):
        super().__init__(2)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],  # Up
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(1, 0)],  # Right
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(0, 1)],  # Down
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(1, 2)],  # Left
        }


class S_Block(Block):
    """S-Block (Green) - S Shape"""
    def __init__(self):
        super().__init__(3)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],  # Horizontal
            1: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)],  # Vertical
            2: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],  # Horizontal
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)],  # Vertical
        }


class Z_Block(Block):
    """Z-Block (Red) - Z Shape"""
    def __init__(self):
        super().__init__(4)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],  # Horizontal
            1: [Position(0, 1), Position(1, 1), Position(1, 0), Position(2, 0)],  # Vertical
            2: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],  # Horizontal
            3: [Position(0, 1), Position(1, 1), Position(1, 0), Position(2, 0)],  # Vertical
        }


class J_Block(Block):
    """J-Block (Blue) - J Shape (left)"""
    def __init__(self):
        super().__init__(5)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(2, 0), Position(2, 1)],  # Down-Right
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],  # Left-Down
            2: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)],  # Up-Left
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)],  # Right-Up
        }


class L_Block(Block):
    """L-Block (Orange) - L Shape (right)"""
    def __init__(self):
        super().__init__(6)
        self.cells = {
            0: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 0)],  # Down-Left
            1: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],  # Right-Down
            2: [Position(0, 0), Position(0, 1), Position(1, 0), Position(2, 0)],  # Up-Right
            3: [Position(0, 0), Position(0, 1), Position(0, 2), Position(1, 2)],  # Left-Up
        }


# Dictionary to create blocks by id
TETRIS_BLOCKS = {
    0: I_Block,
    1: O_Block,
    2: T_Block,
    3: S_Block,
    4: Z_Block,
    5: J_Block,
    6: L_Block,
}

def create_block(block_id):
    """Create a Tetris block by ID (0-6)"""
    if block_id in TETRIS_BLOCKS:
        return TETRIS_BLOCKS[block_id]()
    else:
        raise ValueError(f"Invalid block ID: {block_id}. Must be 0-6.")
