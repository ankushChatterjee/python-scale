"""Tests for module 180."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_180 import subtract_180, modulo_180, power_180, multiply_180

def test_subtract_180():
    assert subtract_180(10, 4) == 6

def test_modulo_180():
    assert modulo_180(10, 3) == 1

def test_power_180():
    assert power_180(2, 8) == 256

def test_multiply_180():
    assert multiply_180(3, 7) == 21
