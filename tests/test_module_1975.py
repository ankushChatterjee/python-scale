"""Tests for test module 1975 — covers src modules [7897, 7898, 7899, 7900]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7897 import add_7897
from module_7898 import subtract_7898
from module_7899 import multiply_7899
from module_7900 import divide_7900

def test_add_7897():
    assert add_7897(2, 3) == 5

def test_subtract_7898():
    assert subtract_7898(10, 4) == 6

def test_multiply_7899():
    assert multiply_7899(3, 7) == 21

def test_divide_7900():
    assert divide_7900(10, 2) == 5.0
