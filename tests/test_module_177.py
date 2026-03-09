"""Tests for module 177."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_177 import subtract_177, power_177, multiply_177, modulo_177

def test_subtract_177():
    assert subtract_177(10, 4) == 6

def test_power_177():
    assert power_177(2, 8) == 256

def test_multiply_177():
    assert multiply_177(3, 7) == 21

def test_modulo_177():
    assert modulo_177(10, 3) == 1
