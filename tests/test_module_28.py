"""Tests for module 28."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_28 import modulo_28, power_28, max_28, divide_28

def test_modulo_28():
    assert modulo_28(10, 3) == 1

def test_power_28():
    assert power_28(2, 8) == 256

def test_max_28():
    assert max_28(3, 7) == 7

def test_divide_28():
    assert divide_28(10, 2) == 5.0
