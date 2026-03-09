"""Tests for module 160."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_160 import add_160, divide_160, modulo_160, power_160

def test_add_160():
    assert add_160(2, 3) == 5

def test_divide_160():
    assert divide_160(10, 2) == 5.0

def test_modulo_160():
    assert modulo_160(10, 3) == 1

def test_power_160():
    assert power_160(2, 8) == 256
