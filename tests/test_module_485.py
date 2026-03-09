"""Tests for test module 485 — covers src modules [1937, 1938, 1939, 1940]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1937 import add_1937
from module_1938 import subtract_1938
from module_1939 import multiply_1939
from module_1940 import divide_1940

def test_add_1937():
    assert add_1937(2, 3) == 5

def test_subtract_1938():
    assert subtract_1938(10, 4) == 6

def test_multiply_1939():
    assert multiply_1939(3, 7) == 21

def test_divide_1940():
    assert divide_1940(10, 2) == 5.0
