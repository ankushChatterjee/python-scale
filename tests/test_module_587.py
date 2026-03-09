"""Tests for test module 587 — covers src modules [2345, 2346, 2347, 2348]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2345 import add_2345
from module_2346 import subtract_2346
from module_2347 import multiply_2347
from module_2348 import divide_2348

def test_add_2345():
    assert add_2345(2, 3) == 5

def test_subtract_2346():
    assert subtract_2346(10, 4) == 6

def test_multiply_2347():
    assert multiply_2347(3, 7) == 21

def test_divide_2348():
    assert divide_2348(10, 2) == 5.0
