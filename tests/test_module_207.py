"""Tests for module 207."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_207 import add_207, power_207, modulo_207, subtract_207

def test_add_207():
    assert add_207(2, 3) == 5

def test_power_207():
    assert power_207(2, 8) == 256

def test_modulo_207():
    assert modulo_207(10, 3) == 1

def test_subtract_207():
    assert subtract_207(10, 4) == 6
