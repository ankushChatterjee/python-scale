"""Tests for module 146."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_146 import max_146, power_146, subtract_146, multiply_146

def test_max_146():
    assert max_146(3, 7) == 7

def test_power_146():
    assert power_146(2, 8) == 256

def test_subtract_146():
    assert subtract_146(10, 4) == 6

def test_multiply_146():
    assert multiply_146(3, 7) == 21
