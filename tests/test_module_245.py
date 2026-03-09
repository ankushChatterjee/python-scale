"""Tests for module 245."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_245 import modulo_245, power_245, divide_245, max_245

def test_modulo_245():
    assert modulo_245(10, 3) == 1

def test_power_245():
    assert power_245(2, 8) == 256

def test_divide_245():
    assert divide_245(10, 2) == 5.0

def test_max_245():
    assert max_245(3, 7) == 7
