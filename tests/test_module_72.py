"""Tests for module 72."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_72 import divide_72, add_72, modulo_72, power_72

def test_divide_72():
    assert divide_72(10, 2) == 5.0

def test_add_72():
    assert add_72(2, 3) == 5

def test_modulo_72():
    assert modulo_72(10, 3) == 1

def test_power_72():
    assert power_72(2, 8) == 256
