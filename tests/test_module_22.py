"""Tests for module 22."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_22 import divide_22, power_22, multiply_22, add_22

def test_divide_22():
    assert divide_22(10, 2) == 5.0

def test_power_22():
    assert power_22(2, 8) == 256

def test_multiply_22():
    assert multiply_22(3, 7) == 21

def test_add_22():
    assert add_22(2, 3) == 5
