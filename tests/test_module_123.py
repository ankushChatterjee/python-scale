"""Tests for module 123."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_123 import modulo_123, power_123, divide_123, multiply_123

def test_modulo_123():
    assert modulo_123(10, 3) == 1

def test_power_123():
    assert power_123(2, 8) == 256

def test_divide_123():
    assert divide_123(10, 2) == 5.0

def test_multiply_123():
    assert multiply_123(3, 7) == 21
