"""Tests for module 98."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_98 import subtract_98, power_98, max_98, modulo_98

def test_subtract_98():
    assert subtract_98(10, 4) == 6

def test_power_98():
    assert power_98(2, 8) == 256

def test_max_98():
    assert max_98(3, 7) == 7

def test_modulo_98():
    assert modulo_98(10, 3) == 1
