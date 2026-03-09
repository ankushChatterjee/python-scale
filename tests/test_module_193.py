"""Tests for module 193."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_193 import divide_193, power_193, max_193, min_193

def test_divide_193():
    assert divide_193(10, 2) == 5.0

def test_power_193():
    assert power_193(2, 8) == 256

def test_max_193():
    assert max_193(3, 7) == 7

def test_min_193():
    assert min_193(3, 7) == 3
