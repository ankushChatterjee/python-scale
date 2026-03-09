"""Tests for module 77."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_77 import divide_77, max_77, add_77, modulo_77

def test_divide_77():
    assert divide_77(10, 2) == 5.0

def test_max_77():
    assert max_77(3, 7) == 7

def test_add_77():
    assert add_77(2, 3) == 5

def test_modulo_77():
    assert modulo_77(10, 3) == 1
