"""Tests for module 250."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_250 import power_250, modulo_250, divide_250, max_250

def test_power_250():
    assert power_250(2, 8) == 256

def test_modulo_250():
    assert modulo_250(10, 3) == 1

def test_divide_250():
    assert divide_250(10, 2) == 5.0

def test_max_250():
    assert max_250(3, 7) == 7
