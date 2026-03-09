"""Tests for module 114."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_114 import power_114, add_114, min_114, multiply_114

def test_power_114():
    assert power_114(2, 8) == 256

def test_add_114():
    assert add_114(2, 3) == 5

def test_min_114():
    assert min_114(3, 7) == 3

def test_multiply_114():
    assert multiply_114(3, 7) == 21
