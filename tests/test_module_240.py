"""Tests for module 240."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_240 import max_240, multiply_240, subtract_240, modulo_240

def test_max_240():
    assert max_240(3, 7) == 7

def test_multiply_240():
    assert multiply_240(3, 7) == 21

def test_subtract_240():
    assert subtract_240(10, 4) == 6

def test_modulo_240():
    assert modulo_240(10, 3) == 1
