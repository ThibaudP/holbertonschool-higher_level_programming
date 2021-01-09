#!/usr/bin/python3
"""lazy_matrix module"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices with NumPy
    """
    print(numpy.version.version)
    return numpy.dot(m_a, m_b)
