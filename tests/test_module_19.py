"""Tests for module 19."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_19 import modulo_19, power_19, min_19, add_19

def test_modulo_19():
    assert modulo_19(10, 3) == 1

def test_power_19():
    assert power_19(2, 8) == 256

def test_min_19():
    assert min_19(3, 7) == 3

def test_add_19():
    assert add_19(2, 3) == 5
