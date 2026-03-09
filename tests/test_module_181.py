"""Tests for module 181."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_181 import add_181, min_181, divide_181, power_181

def test_add_181():
    assert add_181(2, 3) == 5

def test_min_181():
    assert min_181(3, 7) == 3

def test_divide_181():
    assert divide_181(10, 2) == 5.0

def test_power_181():
    assert power_181(2, 8) == 256
