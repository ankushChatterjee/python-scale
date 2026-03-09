"""Tests for module 179."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_179 import power_179, modulo_179, divide_179, multiply_179

def test_power_179():
    assert power_179(2, 8) == 256

def test_modulo_179():
    assert modulo_179(10, 3) == 1

def test_divide_179():
    assert divide_179(10, 2) == 5.0

def test_multiply_179():
    assert multiply_179(3, 7) == 21
