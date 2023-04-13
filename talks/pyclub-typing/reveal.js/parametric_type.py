from typing import TypeVar, Generic

T = TypeVar("T")


RealOrComplex = TypeVar("RealOrComplex", float, complex)


class TwoDVector(Generic[RealOrComplex]):  # syntax to construct parametrized types

    x: RealOrComplex
    y: RealOrComplex

    def __init__(self, x: RealOrComplex, y: RealOrComplex):
        self.x = x
        self.y = y

    def add(self, other: "TwoDVector[RealOrComplex]") -> "TwoDVector[RealOrComplex]":
        return TwoDVector(self.x + other.x, self.y + other.y)


class RealTwoDVector(TwoDVector[float]):
    pass


class ComplexTwoDVector(TwoDVector[complex]):
    pass


real_vec = RealTwoDVector(1.0, 2.0)
complex_vec = ComplexTwoDVector(1.0j, 2.0j)

real_vec.add(real_vec)  # OK
real_vec.add(complex_vec)  # type error
