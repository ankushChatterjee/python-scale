"""Tests for test module 735 — covers src modules [2937, 2938, 2939, 2940]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2937 import add_2937
from module_2938 import subtract_2938
from module_2939 import multiply_2939
from module_2940 import divide_2940

def test_add_2937():
    assert add_2937(2, 3) == 5

def test_subtract_2938():
    assert subtract_2938(10, 4) == 6

def test_multiply_2939():
    assert multiply_2939(3, 7) == 21

def test_divide_2940():
    assert divide_2940(10, 2) == 5.0
