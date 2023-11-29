import numpy as np


class IllegalMove(Exception):
    ...


class Board:
    def __init__(self, n: int = 6, m: int = 7):
        self.state = np.zeros((n, m), dtype=int)


def add_to_board(board: Board, row: int, agent_id: int) -> Board:
    """ Raise IllegalMove exception if move is not possible """
    pass


def is_winning(board: Board) -> bool:
    pass


def is_ended(board: Board) -> bool:
    return not np.isin(0, board.state)
