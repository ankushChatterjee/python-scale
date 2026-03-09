"""Tests for module 143."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_143 import min_143, max_143, modulo_143, divide_143

def test_min_143():
    assert min_143(3, 7) == 3

def test_max_143():
    assert max_143(3, 7) == 7

def test_modulo_143():
    assert modulo_143(10, 3) == 1

def test_divide_143():
    assert divide_143(10, 2) == 5.0
