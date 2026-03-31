from classes.position import Position
from classes.blocks import Block

# Autowygenerowane klasy kształtów z gry Tetris **AI** 
class I_Block(Block):
    """I-Block (Cyan) - 4 tiles in a line"""
    def __init__(self):
        super().__init__(0)
        self.id = 0
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],  # Horizontal
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],  # Vertical
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],  # Horizontal
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)],  # Vertical
        }
        self.move(-1, 3)


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
        self.move(0, 4)


class T_Block(Block):
    """T-Block (Purple) - T Shape"""
    def __init__(self):
        super().__init__(2)
        self.cells = {
            0: [Position(1, 0), Position(0, 1), Position(1, 1), Position(2, 1)],  # Up
            1: [Position(0, 0), Position(0, 1), Position(1, 1), Position(0, 2)],  # Right
            2: [Position(0, 1), Position(1, 1), Position(2, 1), Position(1, 2)],  # Down
            3: [Position(1, 0), Position(0, 1), Position(1, 1), Position(1, 2)],  # Left
        }
        self.move(0, 3)


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
        self.move(0, 3)


class Z_Block(Block):
    """Z-Block (Red) - Z Shape"""
    def __init__(self):
        super().__init__(4)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],  # Horizontal
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],  # Vertical
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],  # Horizontal
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)],  # Vertical
        }
        self.move(0, 3)


class J_Block(Block):
    """J-Block (Blue) - J Shape (left)"""
    def __init__(self):
        super().__init__(5)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)],  # Up
            1: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],  # Right
            2: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)],  # Down
            3: [Position(0, 0), Position(0, 1), Position(0, 2), Position(1, 2)],  # Left
        }
        self.move(0, 3)


class L_Block(Block):
    """L-Block (Orange) - L Shape (right)"""
    def __init__(self):
        super().__init__(6)
        self.cells = {
            0: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)],  # Up
            1: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],  # Right
            2: [Position(0, 0), Position(0, 1), Position(1, 0), Position(2, 0)],  # Down
            3: [Position(0, 0), Position(0, 1), Position(0, 2), Position(1, 0)],  # Left
        }
        self.move(0, 3)


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
