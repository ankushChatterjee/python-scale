"""Tests for module 45."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_45 import multiply_45, power_45, divide_45, modulo_45

def test_multiply_45():
    assert multiply_45(3, 7) == 21

def test_power_45():
    assert power_45(2, 8) == 256

def test_divide_45():
    assert divide_45(10, 2) == 5.0

def test_modulo_45():
    assert modulo_45(10, 3) == 1
