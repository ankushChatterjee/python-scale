"""Tests for module 147."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_147 import max_147, add_147, power_147, multiply_147

def test_max_147():
    assert max_147(3, 7) == 7

def test_add_147():
    assert add_147(2, 3) == 5

def test_power_147():
    assert power_147(2, 8) == 256

def test_multiply_147():
    assert multiply_147(3, 7) == 21
