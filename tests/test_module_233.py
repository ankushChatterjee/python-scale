"""Tests for module 233."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_233 import modulo_233, divide_233, add_233, min_233

def test_modulo_233():
    assert modulo_233(10, 3) == 1

def test_divide_233():
    assert divide_233(10, 2) == 5.0

def test_add_233():
    assert add_233(2, 3) == 5

def test_min_233():
    assert min_233(3, 7) == 3
