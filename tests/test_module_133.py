"""Tests for module 133."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_133 import divide_133, min_133, subtract_133, power_133

def test_divide_133():
    assert divide_133(10, 2) == 5.0

def test_min_133():
    assert min_133(3, 7) == 3

def test_subtract_133():
    assert subtract_133(10, 4) == 6

def test_power_133():
    assert power_133(2, 8) == 256
