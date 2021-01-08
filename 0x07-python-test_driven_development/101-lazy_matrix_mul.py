#!/usr/bin/python3
"""lazy_matrix module"""
from numpy import dot


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices with NumPy
    """
    return dot(m_a, m_b)