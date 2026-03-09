"""Tests for module 241."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_241 import min_241, power_241, divide_241, add_241

def test_min_241():
    assert min_241(3, 7) == 3

def test_power_241():
    assert power_241(2, 8) == 256

def test_divide_241():
    assert divide_241(10, 2) == 5.0

def test_add_241():
    assert add_241(2, 3) == 5
