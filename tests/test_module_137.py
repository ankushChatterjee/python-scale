"""Tests for module 137."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_137 import max_137, divide_137, subtract_137, power_137

def test_max_137():
    assert max_137(3, 7) == 7

def test_divide_137():
    assert divide_137(10, 2) == 5.0

def test_subtract_137():
    assert subtract_137(10, 4) == 6

def test_power_137():
    assert power_137(2, 8) == 256
