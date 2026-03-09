"""Tests for module 144."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_144 import multiply_144, power_144, divide_144, min_144

def test_multiply_144():
    assert multiply_144(3, 7) == 21

def test_power_144():
    assert power_144(2, 8) == 256

def test_divide_144():
    assert divide_144(10, 2) == 5.0

def test_min_144():
    assert min_144(3, 7) == 3
