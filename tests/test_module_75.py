"""Tests for module 75."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_75 import multiply_75, add_75, modulo_75, min_75

def test_multiply_75():
    assert multiply_75(3, 7) == 21

def test_add_75():
    assert add_75(2, 3) == 5

def test_modulo_75():
    assert modulo_75(10, 3) == 1

def test_min_75():
    assert min_75(3, 7) == 3
