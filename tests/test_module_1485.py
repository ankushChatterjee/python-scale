"""Tests for test module 1485 — covers src modules [5937, 5938, 5939, 5940]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5937 import add_5937
from module_5938 import subtract_5938
from module_5939 import multiply_5939
from module_5940 import divide_5940

def test_add_5937():
    assert add_5937(2, 3) == 5

def test_subtract_5938():
    assert subtract_5938(10, 4) == 6

def test_multiply_5939():
    assert multiply_5939(3, 7) == 21

def test_divide_5940():
    assert divide_5940(10, 2) == 5.0
