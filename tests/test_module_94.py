"""Tests for module 94."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_94 import min_94, max_94, multiply_94, add_94

def test_min_94():
    assert min_94(3, 7) == 3

def test_max_94():
    assert max_94(3, 7) == 7

def test_multiply_94():
    assert multiply_94(3, 7) == 21

def test_add_94():
    assert add_94(2, 3) == 5
