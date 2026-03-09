"""Tests for module 165."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_165 import min_165, multiply_165, divide_165, max_165

def test_min_165():
    assert min_165(3, 7) == 3

def test_multiply_165():
    assert multiply_165(3, 7) == 21

def test_divide_165():
    assert divide_165(10, 2) == 5.0

def test_max_165():
    assert max_165(3, 7) == 7
