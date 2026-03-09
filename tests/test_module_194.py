"""Tests for module 194."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_194 import divide_194, power_194, max_194, min_194

def test_divide_194():
    assert divide_194(10, 2) == 5.0

def test_power_194():
    assert power_194(2, 8) == 256

def test_max_194():
    assert max_194(3, 7) == 7

def test_min_194():
    assert min_194(3, 7) == 3
