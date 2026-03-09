"""Tests for module 204."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_204 import modulo_204, power_204, max_204, min_204

def test_modulo_204():
    assert modulo_204(10, 3) == 1

def test_power_204():
    assert power_204(2, 8) == 256

def test_max_204():
    assert max_204(3, 7) == 7

def test_min_204():
    assert min_204(3, 7) == 3
