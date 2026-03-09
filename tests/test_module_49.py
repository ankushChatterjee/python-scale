"""Tests for module 49."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_49 import max_49, modulo_49, divide_49, add_49

def test_max_49():
    assert max_49(3, 7) == 7

def test_modulo_49():
    assert modulo_49(10, 3) == 1

def test_divide_49():
    assert divide_49(10, 2) == 5.0

def test_add_49():
    assert add_49(2, 3) == 5
