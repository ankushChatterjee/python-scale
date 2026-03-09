"""Tests for module 59."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_59 import add_59, power_59, min_59, max_59

def test_add_59():
    assert add_59(2, 3) == 5

def test_power_59():
    assert power_59(2, 8) == 256

def test_min_59():
    assert min_59(3, 7) == 3

def test_max_59():
    assert max_59(3, 7) == 7
