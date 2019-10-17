#!/usr/bin/python3
"""
Print a pascal triangle
"""


def pascal_triangle(n):
    """
    Create a pascal triangle
    """

    triangle = []
    prev_row = [1]
    row = 0
    if n <= 0:
        return []
    triangle.append(prev_row)
    if n == 1:
        return triangle
    while row < n - 1:
        current_row = []
        current_row.append(prev_row[0])
        i = 0
        while i < row:
            current_row.append(prev_row[i] + prev_row[i + 1])
            i += 1
        current_row.append(prev_row[len(prev_row) - 1])
        triangle.append(current_row)
        prev_row = current_row
        row += 1
    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
