"""Tests for test module 739 — covers src modules [2953, 2954, 2955, 2956]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2953 import add_2953
from module_2954 import subtract_2954
from module_2955 import multiply_2955
from module_2956 import divide_2956

def test_add_2953():
    assert add_2953(2, 3) == 5

def test_subtract_2954():
    assert subtract_2954(10, 4) == 6

def test_multiply_2955():
    assert multiply_2955(3, 7) == 21

def test_divide_2956():
    assert divide_2956(10, 2) == 5.0
