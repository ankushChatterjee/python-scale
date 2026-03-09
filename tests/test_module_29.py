"""Tests for module 29."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_29 import min_29, multiply_29, subtract_29, power_29

def test_min_29():
    assert min_29(3, 7) == 3

def test_multiply_29():
    assert multiply_29(3, 7) == 21

def test_subtract_29():
    assert subtract_29(10, 4) == 6

def test_power_29():
    assert power_29(2, 8) == 256
