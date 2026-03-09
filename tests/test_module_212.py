"""Tests for module 212."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_212 import power_212, subtract_212, add_212, multiply_212

def test_power_212():
    assert power_212(2, 8) == 256

def test_subtract_212():
    assert subtract_212(10, 4) == 6

def test_add_212():
    assert add_212(2, 3) == 5

def test_multiply_212():
    assert multiply_212(3, 7) == 21
