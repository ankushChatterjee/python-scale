"""Tests for test module 19 — covers src modules [73, 74, 75, 76]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_73 import add_73
from module_74 import subtract_74
from module_75 import multiply_75
from module_76 import divide_76

def test_add_73():
    assert add_73(2, 3) == 5

def test_subtract_74():
    assert subtract_74(10, 4) == 6

def test_multiply_75():
    assert multiply_75(3, 7) == 21

def test_divide_76():
    assert divide_76(10, 2) == 5.0
