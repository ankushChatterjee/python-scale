"""Tests for module 224."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_224 import subtract_224, max_224, add_224, divide_224

def test_subtract_224():
    assert subtract_224(10, 4) == 6

def test_max_224():
    assert max_224(3, 7) == 7

def test_add_224():
    assert add_224(2, 3) == 5

def test_divide_224():
    assert divide_224(10, 2) == 5.0
