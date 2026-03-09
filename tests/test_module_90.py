"""Tests for module 90."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_90 import subtract_90, power_90, modulo_90, max_90

def test_subtract_90():
    assert subtract_90(10, 4) == 6

def test_power_90():
    assert power_90(2, 8) == 256

def test_modulo_90():
    assert modulo_90(10, 3) == 1

def test_max_90():
    assert max_90(3, 7) == 7
