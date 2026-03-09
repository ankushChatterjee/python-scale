"""Tests for module 110."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_110 import modulo_110, min_110, subtract_110, power_110

def test_modulo_110():
    assert modulo_110(10, 3) == 1

def test_min_110():
    assert min_110(3, 7) == 3

def test_subtract_110():
    assert subtract_110(10, 4) == 6

def test_power_110():
    assert power_110(2, 8) == 256
