"""Tests for module 57."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_57 import divide_57, add_57, min_57, max_57

def test_divide_57():
    assert divide_57(10, 2) == 5.0

def test_add_57():
    assert add_57(2, 3) == 5

def test_min_57():
    assert min_57(3, 7) == 3

def test_max_57():
    assert max_57(3, 7) == 7
