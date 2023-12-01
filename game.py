from base import BaseAgent
from models import Board, is_ended, add_to_board, is_winning

N = 6
M = 7


def run(agents: list[BaseAgent]) -> int | None:
    print(f"Comenzando el juego para los agentes {agents[0].identifier} y {agents[1].identifier}.")
    board = Board(N, M)

    i = 0
    while not is_ended(board):
        idx = i % 2
        acting_agent = agents[idx]

        move = acting_agent.coloca(board)
        add_to_board(board, move, acting_agent.identifier)

        if is_winning(board, move):
            print(f"El agento {acting_agent.identifier} ganó, que bueno.")
            return acting_agent.identifier

        if i > N * M:
            raise Exception("Loop.")
        i += 1

    print("El empante, que triste.")
    return None
