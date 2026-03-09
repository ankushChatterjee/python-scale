"""Tests for module 246."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_246 import add_246, divide_246, max_246, multiply_246

def test_add_246():
    assert add_246(2, 3) == 5

def test_divide_246():
    assert divide_246(10, 2) == 5.0

def test_max_246():
    assert max_246(3, 7) == 7

def test_multiply_246():
    assert multiply_246(3, 7) == 21
