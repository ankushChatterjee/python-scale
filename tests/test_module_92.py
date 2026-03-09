"""Tests for module 92."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_92 import power_92, subtract_92, max_92, multiply_92

def test_power_92():
    assert power_92(2, 8) == 256

def test_subtract_92():
    assert subtract_92(10, 4) == 6

def test_max_92():
    assert max_92(3, 7) == 7

def test_multiply_92():
    assert multiply_92(3, 7) == 21
