"""Tests for module 225."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_225 import max_225, power_225, modulo_225, divide_225

def test_max_225():
    assert max_225(3, 7) == 7

def test_power_225():
    assert power_225(2, 8) == 256

def test_modulo_225():
    assert modulo_225(10, 3) == 1

def test_divide_225():
    assert divide_225(10, 2) == 5.0
