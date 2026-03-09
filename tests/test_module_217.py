"""Tests for module 217."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_217 import min_217, modulo_217, max_217, power_217

def test_min_217():
    assert min_217(3, 7) == 3

def test_modulo_217():
    assert modulo_217(10, 3) == 1

def test_max_217():
    assert max_217(3, 7) == 7

def test_power_217():
    assert power_217(2, 8) == 256
