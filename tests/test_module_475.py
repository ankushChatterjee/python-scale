"""Tests for test module 475 — covers src modules [1897, 1898, 1899, 1900]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1897 import add_1897
from module_1898 import subtract_1898
from module_1899 import multiply_1899
from module_1900 import divide_1900

def test_add_1897():
    assert add_1897(2, 3) == 5

def test_subtract_1898():
    assert subtract_1898(10, 4) == 6

def test_multiply_1899():
    assert multiply_1899(3, 7) == 21

def test_divide_1900():
    assert divide_1900(10, 2) == 5.0
