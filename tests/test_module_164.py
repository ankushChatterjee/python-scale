"""Tests for module 164."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_164 import divide_164, max_164, multiply_164, power_164

def test_divide_164():
    assert divide_164(10, 2) == 5.0

def test_max_164():
    assert max_164(3, 7) == 7

def test_multiply_164():
    assert multiply_164(3, 7) == 21

def test_power_164():
    assert power_164(2, 8) == 256
