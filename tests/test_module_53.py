"""Tests for module 53."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_53 import divide_53, add_53, min_53, multiply_53

def test_divide_53():
    assert divide_53(10, 2) == 5.0

def test_add_53():
    assert add_53(2, 3) == 5

def test_min_53():
    assert min_53(3, 7) == 3

def test_multiply_53():
    assert multiply_53(3, 7) == 21
