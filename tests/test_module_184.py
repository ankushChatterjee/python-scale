"""Tests for module 184."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_184 import modulo_184, max_184, min_184, divide_184

def test_modulo_184():
    assert modulo_184(10, 3) == 1

def test_max_184():
    assert max_184(3, 7) == 7

def test_min_184():
    assert min_184(3, 7) == 3

def test_divide_184():
    assert divide_184(10, 2) == 5.0
