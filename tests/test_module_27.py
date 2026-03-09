"""Tests for module 27."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_27 import modulo_27, subtract_27, min_27, max_27

def test_modulo_27():
    assert modulo_27(10, 3) == 1

def test_subtract_27():
    assert subtract_27(10, 4) == 6

def test_min_27():
    assert min_27(3, 7) == 3

def test_max_27():
    assert max_27(3, 7) == 7
