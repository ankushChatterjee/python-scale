"""Tests for module 34."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_34 import add_34, power_34, min_34, max_34

def test_add_34():
    assert add_34(2, 3) == 5

def test_power_34():
    assert power_34(2, 8) == 256

def test_min_34():
    assert min_34(3, 7) == 3

def test_max_34():
    assert max_34(3, 7) == 7
