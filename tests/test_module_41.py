"""Tests for module 41."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_41 import add_41, max_41, multiply_41, power_41

def test_add_41():
    assert add_41(2, 3) == 5

def test_max_41():
    assert max_41(3, 7) == 7

def test_multiply_41():
    assert multiply_41(3, 7) == 21

def test_power_41():
    assert power_41(2, 8) == 256
