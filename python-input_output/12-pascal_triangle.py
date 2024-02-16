#!/usr/bin/python3
"""Defines a pascal_triangle function"""


def pascal_triangle(n):
    """Represents a pascal triangle"""
    new_matrix = []
    if n <= 0:
        return new_matrix
    new_matrix = [[1]]
    for i in range(1, n):
        rows = [1]
        for j in range(len(new_matrix[i - 1]) - 1):
            current = new_matrix[i - 1]
            rows.append(new_matrix[i - 1][j] + new_matrix[i - 1][j + 1])
        rows.append(1)
        new_matrix.append(rows)
    return new_matrix
