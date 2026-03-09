"""Tests for module 99."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_99 import add_99, min_99, multiply_99, modulo_99

def test_add_99():
    assert add_99(2, 3) == 5

def test_min_99():
    assert min_99(3, 7) == 3

def test_multiply_99():
    assert multiply_99(3, 7) == 21

def test_modulo_99():
    assert modulo_99(10, 3) == 1
