"""Tests for module 156."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_156 import divide_156, max_156, subtract_156, multiply_156

def test_divide_156():
    assert divide_156(10, 2) == 5.0

def test_max_156():
    assert max_156(3, 7) == 7

def test_subtract_156():
    assert subtract_156(10, 4) == 6

def test_multiply_156():
    assert multiply_156(3, 7) == 21
