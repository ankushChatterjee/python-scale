"""Tests for module 127."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_127 import min_127, modulo_127, add_127, multiply_127

def test_min_127():
    assert min_127(3, 7) == 3

def test_modulo_127():
    assert modulo_127(10, 3) == 1

def test_add_127():
    assert add_127(2, 3) == 5

def test_multiply_127():
    assert multiply_127(3, 7) == 21
