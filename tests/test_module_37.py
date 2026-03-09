"""Tests for module 37."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_37 import max_37, add_37, power_37, multiply_37

def test_max_37():
    assert max_37(3, 7) == 7

def test_add_37():
    assert add_37(2, 3) == 5

def test_power_37():
    assert power_37(2, 8) == 256

def test_multiply_37():
    assert multiply_37(3, 7) == 21
