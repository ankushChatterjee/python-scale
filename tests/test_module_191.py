"""Tests for module 191."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_191 import modulo_191, max_191, power_191, multiply_191

def test_modulo_191():
    assert modulo_191(10, 3) == 1

def test_max_191():
    assert max_191(3, 7) == 7

def test_power_191():
    assert power_191(2, 8) == 256

def test_multiply_191():
    assert multiply_191(3, 7) == 21
