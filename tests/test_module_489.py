"""Tests for test module 489 — covers src modules [1953, 1954, 1955, 1956]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1953 import add_1953
from module_1954 import subtract_1954
from module_1955 import multiply_1955
from module_1956 import divide_1956

def test_add_1953():
    assert add_1953(2, 3) == 5

def test_subtract_1954():
    assert subtract_1954(10, 4) == 6

def test_multiply_1955():
    assert multiply_1955(3, 7) == 21

def test_divide_1956():
    assert divide_1956(10, 2) == 5.0
