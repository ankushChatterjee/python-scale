"""Tests for module 51."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_51 import add_51, modulo_51, min_51, subtract_51

def test_add_51():
    assert add_51(2, 3) == 5

def test_modulo_51():
    assert modulo_51(10, 3) == 1

def test_min_51():
    assert min_51(3, 7) == 3

def test_subtract_51():
    assert subtract_51(10, 4) == 6
