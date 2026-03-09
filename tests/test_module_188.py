"""Tests for module 188."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_188 import min_188, multiply_188, add_188, divide_188

def test_min_188():
    assert min_188(3, 7) == 3

def test_multiply_188():
    assert multiply_188(3, 7) == 21

def test_add_188():
    assert add_188(2, 3) == 5

def test_divide_188():
    assert divide_188(10, 2) == 5.0
