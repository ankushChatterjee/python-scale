"""Tests for module 136."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_136 import divide_136, power_136, min_136, max_136

def test_divide_136():
    assert divide_136(10, 2) == 5.0

def test_power_136():
    assert power_136(2, 8) == 256

def test_min_136():
    assert min_136(3, 7) == 3

def test_max_136():
    assert max_136(3, 7) == 7
