"""Tests for test module 743 — covers src modules [2969, 2970, 2971, 2972]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2969 import add_2969
from module_2970 import subtract_2970
from module_2971 import multiply_2971
from module_2972 import divide_2972

def test_add_2969():
    assert add_2969(2, 3) == 5

def test_subtract_2970():
    assert subtract_2970(10, 4) == 6

def test_multiply_2971():
    assert multiply_2971(3, 7) == 21

def test_divide_2972():
    assert divide_2972(10, 2) == 5.0
