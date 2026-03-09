"""Tests for module 163."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_163 import add_163, multiply_163, divide_163, min_163

def test_add_163():
    assert add_163(2, 3) == 5

def test_multiply_163():
    assert multiply_163(3, 7) == 21

def test_divide_163():
    assert divide_163(10, 2) == 5.0

def test_min_163():
    assert min_163(3, 7) == 3
