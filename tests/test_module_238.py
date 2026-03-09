"""Tests for module 238."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_238 import add_238, min_238, power_238, multiply_238

def test_add_238():
    assert add_238(2, 3) == 5

def test_min_238():
    assert min_238(3, 7) == 3

def test_power_238():
    assert power_238(2, 8) == 256

def test_multiply_238():
    assert multiply_238(3, 7) == 21
