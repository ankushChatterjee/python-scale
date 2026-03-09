"""Tests for test module 1931 — covers src modules [7721, 7722, 7723, 7724]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7721 import add_7721
from module_7722 import subtract_7722
from module_7723 import multiply_7723
from module_7724 import divide_7724

def test_add_7721():
    assert add_7721(2, 3) == 5

def test_subtract_7722():
    assert subtract_7722(10, 4) == 6

def test_multiply_7723():
    assert multiply_7723(3, 7) == 21

def test_divide_7724():
    assert divide_7724(10, 2) == 5.0
