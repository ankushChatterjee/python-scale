"""Tests for module 67."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_67 import min_67, divide_67, max_67, subtract_67

def test_min_67():
    assert min_67(3, 7) == 3

def test_divide_67():
    assert divide_67(10, 2) == 5.0

def test_max_67():
    assert max_67(3, 7) == 7

def test_subtract_67():
    assert subtract_67(10, 4) == 6
