"""Tests for module 87."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_87 import max_87, min_87, modulo_87, multiply_87

def test_max_87():
    assert max_87(3, 7) == 7

def test_min_87():
    assert min_87(3, 7) == 3

def test_modulo_87():
    assert modulo_87(10, 3) == 1

def test_multiply_87():
    assert multiply_87(3, 7) == 21
