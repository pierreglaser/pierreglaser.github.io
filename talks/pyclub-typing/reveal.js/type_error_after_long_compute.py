import numpy as np


def heavy_op_and_type_error():
    large_matrix = np.random.rand(1000, 1000)
    result = large_matrix @ large_matrix  # O(n³) operations!
    1 + "OK"  # raises TypeError: unsupported operand type(s) for +: 'int' and 'str'
    return result


if __name__ == "__main__":
    heavy_op_and_type_error()
