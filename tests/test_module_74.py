"""Tests for module 74."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_74 import add_74, modulo_74, divide_74, min_74

def test_add_74():
    assert add_74(2, 3) == 5

def test_modulo_74():
    assert modulo_74(10, 3) == 1

def test_divide_74():
    assert divide_74(10, 2) == 5.0

def test_min_74():
    assert min_74(3, 7) == 3
