"""Tests for module 244."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_244 import power_244, divide_244, max_244, min_244

def test_power_244():
    assert power_244(2, 8) == 256

def test_divide_244():
    assert divide_244(10, 2) == 5.0

def test_max_244():
    assert max_244(3, 7) == 7

def test_min_244():
    assert min_244(3, 7) == 3
