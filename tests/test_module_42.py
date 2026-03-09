"""Tests for module 42."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_42 import divide_42, add_42, subtract_42, modulo_42

def test_divide_42():
    assert divide_42(10, 2) == 5.0

def test_add_42():
    assert add_42(2, 3) == 5

def test_subtract_42():
    assert subtract_42(10, 4) == 6

def test_modulo_42():
    assert modulo_42(10, 3) == 1
