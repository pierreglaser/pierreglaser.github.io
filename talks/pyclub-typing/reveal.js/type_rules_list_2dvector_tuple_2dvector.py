from functools import reduce
from typing import List, Union

from typing_extensions import Self


class TwoDVector:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"TwoDVector({self.x}, {self.y})"

    def add(self: Self, other: Self) -> Self:
        return TwoDVector(self.x + other.x, self.y + other.y)


class ThreeDVector:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"ThreeDVector({self.x}, {self.y}, {self.z})"

    def add(self: Self, other: Self) -> Self:
        return ThreeDVector(self.x + other.x, self.y + other.y, self.z + other.z)


TwoOrThreeDVector = Union[TwoDVector, ThreeDVector]


class ListOfTwoDVector:
    def __getitem__(self, index: int) -> TwoDVector:
        ...

    def __setitem__(self, index: int, value: TwoDVector) -> "ListOfTwoDVector":
        ...


class TupleOfTwoDVector:
    def __getitem__(self, index: int) -> TwoDVector:
        ...

class TupleOfTwoOrThreeDVector:
    def __getitem__(self, index: int) -> TwoOrThreeDVector:
        ...
