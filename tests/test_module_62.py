"""Tests for module 62."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_62 import max_62, subtract_62, divide_62, min_62

def test_max_62():
    assert max_62(3, 7) == 7

def test_subtract_62():
    assert subtract_62(10, 4) == 6

def test_divide_62():
    assert divide_62(10, 2) == 5.0

def test_min_62():
    assert min_62(3, 7) == 3
