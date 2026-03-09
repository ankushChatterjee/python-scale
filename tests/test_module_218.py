"""Tests for module 218."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_218 import divide_218, min_218, modulo_218, max_218

def test_divide_218():
    assert divide_218(10, 2) == 5.0

def test_min_218():
    assert min_218(3, 7) == 3

def test_modulo_218():
    assert modulo_218(10, 3) == 1

def test_max_218():
    assert max_218(3, 7) == 7
