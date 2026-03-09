"""Tests for module 131."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_131 import subtract_131, multiply_131, modulo_131, power_131

def test_subtract_131():
    assert subtract_131(10, 4) == 6

def test_multiply_131():
    assert multiply_131(3, 7) == 21

def test_modulo_131():
    assert modulo_131(10, 3) == 1

def test_power_131():
    assert power_131(2, 8) == 256
