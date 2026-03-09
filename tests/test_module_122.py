"""Tests for module 122."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_122 import power_122, max_122, add_122, multiply_122

def test_power_122():
    assert power_122(2, 8) == 256

def test_max_122():
    assert max_122(3, 7) == 7

def test_add_122():
    assert add_122(2, 3) == 5

def test_multiply_122():
    assert multiply_122(3, 7) == 21
