from base import BaseAgent
from game import run


class DummyAgent(BaseAgent):
    def __init__(self, identifier: int):
        self._identifier = identifier


    @property
    def identifier(self) -> int:
        return self._identifier

    def coloca(self, board):
        return self.identifier
    pass


if __name__ == '__main__':
    agents = (DummyAgent(0), DummyAgent(1))
    run(agents)
