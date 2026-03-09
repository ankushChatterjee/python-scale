"""Tests for module 232."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_232 import modulo_232, max_232, power_232, min_232

def test_modulo_232():
    assert modulo_232(10, 3) == 1

def test_max_232():
    assert max_232(3, 7) == 7

def test_power_232():
    assert power_232(2, 8) == 256

def test_min_232():
    assert min_232(3, 7) == 3
