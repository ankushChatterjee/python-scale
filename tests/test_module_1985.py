"""Tests for test module 1985 — covers src modules [7937, 7938, 7939, 7940]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7937 import add_7937
from module_7938 import subtract_7938
from module_7939 import multiply_7939
from module_7940 import divide_7940

def test_add_7937():
    assert add_7937(2, 3) == 5

def test_subtract_7938():
    assert subtract_7938(10, 4) == 6

def test_multiply_7939():
    assert multiply_7939(3, 7) == 21

def test_divide_7940():
    assert divide_7940(10, 2) == 5.0
