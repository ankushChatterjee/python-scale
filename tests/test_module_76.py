"""Tests for module 76."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_76 import multiply_76, add_76, modulo_76, min_76

def test_multiply_76():
    assert multiply_76(3, 7) == 21

def test_add_76():
    assert add_76(2, 3) == 5

def test_modulo_76():
    assert modulo_76(10, 3) == 1

def test_min_76():
    assert min_76(3, 7) == 3
