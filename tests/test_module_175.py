"""Tests for module 175."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_175 import min_175, divide_175, power_175, subtract_175

def test_min_175():
    assert min_175(3, 7) == 3

def test_divide_175():
    assert divide_175(10, 2) == 5.0

def test_power_175():
    assert power_175(2, 8) == 256

def test_subtract_175():
    assert subtract_175(10, 4) == 6
