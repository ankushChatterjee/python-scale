"""Tests for test module 1235 — covers src modules [4937, 4938, 4939, 4940]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4937 import add_4937
from module_4938 import subtract_4938
from module_4939 import multiply_4939
from module_4940 import divide_4940

def test_add_4937():
    assert add_4937(2, 3) == 5

def test_subtract_4938():
    assert subtract_4938(10, 4) == 6

def test_multiply_4939():
    assert multiply_4939(3, 7) == 21

def test_divide_4940():
    assert divide_4940(10, 2) == 5.0
