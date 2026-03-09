"""Tests for module 107."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_107 import modulo_107, subtract_107, power_107, add_107

def test_modulo_107():
    assert modulo_107(10, 3) == 1

def test_subtract_107():
    assert subtract_107(10, 4) == 6

def test_power_107():
    assert power_107(2, 8) == 256

def test_add_107():
    assert add_107(2, 3) == 5
