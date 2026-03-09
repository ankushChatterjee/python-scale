"""Tests for test module 1725 — covers src modules [6897, 6898, 6899, 6900]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6897 import add_6897
from module_6898 import subtract_6898
from module_6899 import multiply_6899
from module_6900 import divide_6900

def test_add_6897():
    assert add_6897(2, 3) == 5

def test_subtract_6898():
    assert subtract_6898(10, 4) == 6

def test_multiply_6899():
    assert multiply_6899(3, 7) == 21

def test_divide_6900():
    assert divide_6900(10, 2) == 5.0
