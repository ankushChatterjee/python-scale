"""Tests for module 3."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3 import subtract_3, modulo_3, divide_3, add_3

def test_subtract_3():
    assert subtract_3(10, 4) == 6

def test_modulo_3():
    assert modulo_3(10, 3) == 1

def test_divide_3():
    assert divide_3(10, 2) == 5.0

def test_add_3():
    assert add_3(2, 3) == 5
