"""Tests for test module 1735 — covers src modules [6937, 6938, 6939, 6940]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6937 import add_6937
from module_6938 import subtract_6938
from module_6939 import multiply_6939
from module_6940 import divide_6940

def test_add_6937():
    assert add_6937(2, 3) == 5

def test_subtract_6938():
    assert subtract_6938(10, 4) == 6

def test_multiply_6939():
    assert multiply_6939(3, 7) == 21

def test_divide_6940():
    assert divide_6940(10, 2) == 5.0
