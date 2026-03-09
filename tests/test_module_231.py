"""Tests for module 231."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_231 import multiply_231, add_231, min_231, subtract_231

def test_multiply_231():
    assert multiply_231(3, 7) == 21

def test_add_231():
    assert add_231(2, 3) == 5

def test_min_231():
    assert min_231(3, 7) == 3

def test_subtract_231():
    assert subtract_231(10, 4) == 6
