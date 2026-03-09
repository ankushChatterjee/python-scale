"""Tests for module 12."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_12 import max_12, modulo_12, add_12, divide_12

def test_max_12():
    assert max_12(3, 7) == 7

def test_modulo_12():
    assert modulo_12(10, 3) == 1

def test_add_12():
    assert add_12(2, 3) == 5

def test_divide_12():
    assert divide_12(10, 2) == 5.0
