"""Tests for module 73."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_73 import add_73, power_73, multiply_73, max_73

def test_add_73():
    assert add_73(2, 3) == 5

def test_power_73():
    assert power_73(2, 8) == 256

def test_multiply_73():
    assert multiply_73(3, 7) == 21

def test_max_73():
    assert max_73(3, 7) == 7
