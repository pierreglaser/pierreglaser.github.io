from typing import List
from typing_extensions import Self
from functools import reduce


class 2DVector:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"2DVector({self.x}, {self.y})"

    def add(self: Self, other: Self) -> Self:
        return 2DVector(self.x + other.x, self.y + other.y)


ListOf2DVector = List[2DVector]


def add_all(l: ListOf2DVector) -> 2DVector:
    return reduce(lambda x, y: x.add(y), l)


if __name__ == "__main__":
    l = [2DVector(1, 2), 2DVector(3, 4), 2DVector(5, 6)]
    print(add_all(l))
