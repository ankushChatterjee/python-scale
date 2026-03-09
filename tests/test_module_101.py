"""Tests for module 101."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_101 import modulo_101, multiply_101, add_101, min_101

def test_modulo_101():
    assert modulo_101(10, 3) == 1

def test_multiply_101():
    assert multiply_101(3, 7) == 21

def test_add_101():
    assert add_101(2, 3) == 5

def test_min_101():
    assert min_101(3, 7) == 3
