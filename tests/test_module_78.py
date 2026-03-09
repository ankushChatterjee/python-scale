"""Tests for module 78."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_78 import divide_78, modulo_78, min_78, add_78

def test_divide_78():
    assert divide_78(10, 2) == 5.0

def test_modulo_78():
    assert modulo_78(10, 3) == 1

def test_min_78():
    assert min_78(3, 7) == 3

def test_add_78():
    assert add_78(2, 3) == 5
