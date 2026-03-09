"""Tests for module 88."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_88 import add_88, power_88, modulo_88, multiply_88

def test_add_88():
    assert add_88(2, 3) == 5

def test_power_88():
    assert power_88(2, 8) == 256

def test_modulo_88():
    assert modulo_88(10, 3) == 1

def test_multiply_88():
    assert multiply_88(3, 7) == 21
