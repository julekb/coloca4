from abc import abstractmethod
from typing import Protocol

from models import Board


class BaseAgent(Protocol):
    """ Use this as a base model for your own Coloca4 agent implementation."""
    @property
    def identifier(self) -> int:
        ...

    @abstractmethod
    def coloca(self, board: Board) -> int:
        ...
