from __future__ import annotations

from typing import List


class Matrix:

    def __init__(self, matrix: List[List[float]]) -> None:
        self.matrix = matrix

    def __mul__(self, m: Matrix | int) -> Matrix:
        return self

    def __add__(self, m: Matrix) -> Matrix:
        return self

    def __invert__(self) -> Matrix:
        pass
