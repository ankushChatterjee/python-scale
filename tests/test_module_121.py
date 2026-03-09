"""Tests for module 121."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_121 import power_121, divide_121, add_121, multiply_121

def test_power_121():
    assert power_121(2, 8) == 256

def test_divide_121():
    assert divide_121(10, 2) == 5.0

def test_add_121():
    assert add_121(2, 3) == 5

def test_multiply_121():
    assert multiply_121(3, 7) == 21
