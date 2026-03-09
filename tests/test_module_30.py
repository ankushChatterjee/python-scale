"""Tests for module 30."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_30 import max_30, add_30, min_30, power_30

def test_max_30():
    assert max_30(3, 7) == 7

def test_add_30():
    assert add_30(2, 3) == 5

def test_min_30():
    assert min_30(3, 7) == 3

def test_power_30():
    assert power_30(2, 8) == 256
