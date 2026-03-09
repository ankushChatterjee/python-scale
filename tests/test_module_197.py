"""Tests for module 197."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_197 import modulo_197, power_197, max_197, multiply_197

def test_modulo_197():
    assert modulo_197(10, 3) == 1

def test_power_197():
    assert power_197(2, 8) == 256

def test_max_197():
    assert max_197(3, 7) == 7

def test_multiply_197():
    assert multiply_197(3, 7) == 21
