"""Tests for module 239."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_239 import add_239, min_239, subtract_239, divide_239

def test_add_239():
    assert add_239(2, 3) == 5

def test_min_239():
    assert min_239(3, 7) == 3

def test_subtract_239():
    assert subtract_239(10, 4) == 6

def test_divide_239():
    assert divide_239(10, 2) == 5.0
