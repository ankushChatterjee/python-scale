"""Tests for test module 725 — covers src modules [2897, 2898, 2899, 2900]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2897 import add_2897
from module_2898 import subtract_2898
from module_2899 import multiply_2899
from module_2900 import divide_2900

def test_add_2897():
    assert add_2897(2, 3) == 5

def test_subtract_2898():
    assert subtract_2898(10, 4) == 6

def test_multiply_2899():
    assert multiply_2899(3, 7) == 21

def test_divide_2900():
    assert divide_2900(10, 2) == 5.0
