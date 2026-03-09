"""Tests for module 157."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_157 import min_157, divide_157, add_157, max_157

def test_min_157():
    assert min_157(3, 7) == 3

def test_divide_157():
    assert divide_157(10, 2) == 5.0

def test_add_157():
    assert add_157(2, 3) == 5

def test_max_157():
    assert max_157(3, 7) == 7
