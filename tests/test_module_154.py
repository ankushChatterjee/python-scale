"""Tests for module 154."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_154 import min_154, divide_154, add_154, multiply_154

def test_min_154():
    assert min_154(3, 7) == 3

def test_divide_154():
    assert divide_154(10, 2) == 5.0

def test_add_154():
    assert add_154(2, 3) == 5

def test_multiply_154():
    assert multiply_154(3, 7) == 21
