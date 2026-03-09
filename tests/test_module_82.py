"""Tests for module 82."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_82 import modulo_82, divide_82, multiply_82, add_82

def test_modulo_82():
    assert modulo_82(10, 3) == 1

def test_divide_82():
    assert divide_82(10, 2) == 5.0

def test_multiply_82():
    assert multiply_82(3, 7) == 21

def test_add_82():
    assert add_82(2, 3) == 5
