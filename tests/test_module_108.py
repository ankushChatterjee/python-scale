"""Tests for module 108."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_108 import min_108, max_108, add_108, divide_108

def test_min_108():
    assert min_108(3, 7) == 3

def test_max_108():
    assert max_108(3, 7) == 7

def test_add_108():
    assert add_108(2, 3) == 5

def test_divide_108():
    assert divide_108(10, 2) == 5.0
