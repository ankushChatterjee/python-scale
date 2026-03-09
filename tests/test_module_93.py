"""Tests for module 93."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_93 import max_93, multiply_93, add_93, power_93

def test_max_93():
    assert max_93(3, 7) == 7

def test_multiply_93():
    assert multiply_93(3, 7) == 21

def test_add_93():
    assert add_93(2, 3) == 5

def test_power_93():
    assert power_93(2, 8) == 256
