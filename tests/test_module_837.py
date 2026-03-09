"""Tests for test module 837 — covers src modules [3345, 3346, 3347, 3348]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3345 import add_3345
from module_3346 import subtract_3346
from module_3347 import multiply_3347
from module_3348 import divide_3348

def test_add_3345():
    assert add_3345(2, 3) == 5

def test_subtract_3346():
    assert subtract_3346(10, 4) == 6

def test_multiply_3347():
    assert multiply_3347(3, 7) == 21

def test_divide_3348():
    assert divide_3348(10, 2) == 5.0
