"""Tests for module 96."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_96 import multiply_96, power_96, divide_96, modulo_96

def test_multiply_96():
    assert multiply_96(3, 7) == 21

def test_power_96():
    assert power_96(2, 8) == 256

def test_divide_96():
    assert divide_96(10, 2) == 5.0

def test_modulo_96():
    assert modulo_96(10, 3) == 1
