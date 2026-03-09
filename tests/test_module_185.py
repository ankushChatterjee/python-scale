"""Tests for module 185."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_185 import max_185, divide_185, power_185, modulo_185

def test_max_185():
    assert max_185(3, 7) == 7

def test_divide_185():
    assert divide_185(10, 2) == 5.0

def test_power_185():
    assert power_185(2, 8) == 256

def test_modulo_185():
    assert modulo_185(10, 3) == 1
