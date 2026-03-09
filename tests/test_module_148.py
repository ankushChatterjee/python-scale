"""Tests for module 148."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_148 import divide_148, multiply_148, min_148, power_148

def test_divide_148():
    assert divide_148(10, 2) == 5.0

def test_multiply_148():
    assert multiply_148(3, 7) == 21

def test_min_148():
    assert min_148(3, 7) == 3

def test_power_148():
    assert power_148(2, 8) == 256
