"""Tests for module 16."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_16 import subtract_16, min_16, max_16, add_16

def test_subtract_16():
    assert subtract_16(10, 4) == 6

def test_min_16():
    assert min_16(3, 7) == 3

def test_max_16():
    assert max_16(3, 7) == 7

def test_add_16():
    assert add_16(2, 3) == 5
