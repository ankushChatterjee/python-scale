"""Tests for module 173."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_173 import subtract_173, min_173, max_173, multiply_173

def test_subtract_173():
    assert subtract_173(10, 4) == 6

def test_min_173():
    assert min_173(3, 7) == 3

def test_max_173():
    assert max_173(3, 7) == 7

def test_multiply_173():
    assert multiply_173(3, 7) == 21
