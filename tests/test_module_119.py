"""Tests for module 119."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_119 import modulo_119, add_119, power_119, divide_119

def test_modulo_119():
    assert modulo_119(10, 3) == 1

def test_add_119():
    assert add_119(2, 3) == 5

def test_power_119():
    assert power_119(2, 8) == 256

def test_divide_119():
    assert divide_119(10, 2) == 5.0
