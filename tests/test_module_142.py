"""Tests for module 142."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_142 import power_142, min_142, divide_142, modulo_142

def test_power_142():
    assert power_142(2, 8) == 256

def test_min_142():
    assert min_142(3, 7) == 3

def test_divide_142():
    assert divide_142(10, 2) == 5.0

def test_modulo_142():
    assert modulo_142(10, 3) == 1
