"""Tests for test module 985 — covers src modules [3937, 3938, 3939, 3940]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3937 import add_3937
from module_3938 import subtract_3938
from module_3939 import multiply_3939
from module_3940 import divide_3940

def test_add_3937():
    assert add_3937(2, 3) == 5

def test_subtract_3938():
    assert subtract_3938(10, 4) == 6

def test_multiply_3939():
    assert multiply_3939(3, 7) == 21

def test_divide_3940():
    assert divide_3940(10, 2) == 5.0
