"""Tests for module 83."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_83 import add_83, divide_83, modulo_83, power_83

def test_add_83():
    assert add_83(2, 3) == 5

def test_divide_83():
    assert divide_83(10, 2) == 5.0

def test_modulo_83():
    assert modulo_83(10, 3) == 1

def test_power_83():
    assert power_83(2, 8) == 256
