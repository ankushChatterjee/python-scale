"""Tests for module 200."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_200 import power_200, max_200, divide_200, multiply_200

def test_power_200():
    assert power_200(2, 8) == 256

def test_max_200():
    assert max_200(3, 7) == 7

def test_divide_200():
    assert divide_200(10, 2) == 5.0

def test_multiply_200():
    assert multiply_200(3, 7) == 21
