"""Tests for module 70."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_70 import modulo_70, divide_70, power_70, max_70

def test_modulo_70():
    assert modulo_70(10, 3) == 1

def test_divide_70():
    assert divide_70(10, 2) == 5.0

def test_power_70():
    assert power_70(2, 8) == 256

def test_max_70():
    assert max_70(3, 7) == 7
