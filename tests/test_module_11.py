"""Tests for module 11."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_11 import power_11, modulo_11, multiply_11, add_11

def test_power_11():
    assert power_11(2, 8) == 256

def test_modulo_11():
    assert modulo_11(10, 3) == 1

def test_multiply_11():
    assert multiply_11(3, 7) == 21

def test_add_11():
    assert add_11(2, 3) == 5
