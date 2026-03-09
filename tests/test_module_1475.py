"""Tests for test module 1475 — covers src modules [5897, 5898, 5899, 5900]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5897 import add_5897
from module_5898 import subtract_5898
from module_5899 import multiply_5899
from module_5900 import divide_5900

def test_add_5897():
    assert add_5897(2, 3) == 5

def test_subtract_5898():
    assert subtract_5898(10, 4) == 6

def test_multiply_5899():
    assert multiply_5899(3, 7) == 21

def test_divide_5900():
    assert divide_5900(10, 2) == 5.0
