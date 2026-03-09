"""Tests for test module 235 — covers src modules [937, 938, 939, 940]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_937 import add_937
from module_938 import subtract_938
from module_939 import multiply_939
from module_940 import divide_940

def test_add_937():
    assert add_937(2, 3) == 5

def test_subtract_938():
    assert subtract_938(10, 4) == 6

def test_multiply_939():
    assert multiply_939(3, 7) == 21

def test_divide_940():
    assert divide_940(10, 2) == 5.0
