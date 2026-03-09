"""Tests for module 195."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_195 import max_195, min_195, add_195, power_195

def test_max_195():
    assert max_195(3, 7) == 7

def test_min_195():
    assert min_195(3, 7) == 3

def test_add_195():
    assert add_195(2, 3) == 5

def test_power_195():
    assert power_195(2, 8) == 256
