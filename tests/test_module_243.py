"""Tests for module 243."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_243 import power_243, max_243, add_243, subtract_243

def test_power_243():
    assert power_243(2, 8) == 256

def test_max_243():
    assert max_243(3, 7) == 7

def test_add_243():
    assert add_243(2, 3) == 5

def test_subtract_243():
    assert subtract_243(10, 4) == 6
