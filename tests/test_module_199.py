"""Tests for module 199."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_199 import min_199, power_199, modulo_199, multiply_199

def test_min_199():
    assert min_199(3, 7) == 3

def test_power_199():
    assert power_199(2, 8) == 256

def test_modulo_199():
    assert modulo_199(10, 3) == 1

def test_multiply_199():
    assert multiply_199(3, 7) == 21
