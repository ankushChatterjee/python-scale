"""Tests for module 169."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_169 import divide_169, min_169, add_169, modulo_169

def test_divide_169():
    assert divide_169(10, 2) == 5.0

def test_min_169():
    assert min_169(3, 7) == 3

def test_add_169():
    assert add_169(2, 3) == 5

def test_modulo_169():
    assert modulo_169(10, 3) == 1
