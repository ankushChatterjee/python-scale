"""Tests for module 176."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_176 import subtract_176, modulo_176, power_176, max_176

def test_subtract_176():
    assert subtract_176(10, 4) == 6

def test_modulo_176():
    assert modulo_176(10, 3) == 1

def test_power_176():
    assert power_176(2, 8) == 256

def test_max_176():
    assert max_176(3, 7) == 7
