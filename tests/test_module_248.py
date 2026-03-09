"""Tests for module 248."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_248 import add_248, power_248, modulo_248, divide_248

def test_add_248():
    assert add_248(2, 3) == 5

def test_power_248():
    assert power_248(2, 8) == 256

def test_modulo_248():
    assert modulo_248(10, 3) == 1

def test_divide_248():
    assert divide_248(10, 2) == 5.0
