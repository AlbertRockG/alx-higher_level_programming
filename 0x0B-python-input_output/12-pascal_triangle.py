#!/usr/bin/python3
# 12-pascal_triangle.py
# AlbertRockG
"""Defines a Pascal's triangle solving function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n (int): The number of row of the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangles = []
    for i in range(n):
        next_row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                next_row.append(1)
            else:
                next_row.append(
                        triangles[i-1][j-1] + triangles[i-1][j]
                        )
        triangles.append(next_row)
    return triangles
