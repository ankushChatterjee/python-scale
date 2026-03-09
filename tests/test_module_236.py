"""Tests for module 236."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_236 import add_236, divide_236, power_236, multiply_236

def test_add_236():
    assert add_236(2, 3) == 5

def test_divide_236():
    assert divide_236(10, 2) == 5.0

def test_power_236():
    assert power_236(2, 8) == 256

def test_multiply_236():
    assert multiply_236(3, 7) == 21
