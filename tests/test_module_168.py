"""Tests for module 168."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_168 import add_168, min_168, max_168, subtract_168

def test_add_168():
    assert add_168(2, 3) == 5

def test_min_168():
    assert min_168(3, 7) == 3

def test_max_168():
    assert max_168(3, 7) == 7

def test_subtract_168():
    assert subtract_168(10, 4) == 6
