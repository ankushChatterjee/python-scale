"""Tests for test module 2235 — covers src modules [8937, 8938, 8939, 8940]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8937 import add_8937
from module_8938 import subtract_8938
from module_8939 import multiply_8939
from module_8940 import divide_8940

def test_add_8937():
    assert add_8937(2, 3) == 5

def test_subtract_8938():
    assert subtract_8938(10, 4) == 6

def test_multiply_8939():
    assert multiply_8939(3, 7) == 21

def test_divide_8940():
    assert divide_8940(10, 2) == 5.0
