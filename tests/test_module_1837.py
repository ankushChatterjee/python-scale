"""Tests for test module 1837 — covers src modules [7345, 7346, 7347, 7348]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7345 import add_7345
from module_7346 import subtract_7346
from module_7347 import multiply_7347
from module_7348 import divide_7348

def test_add_7345():
    assert add_7345(2, 3) == 5

def test_subtract_7346():
    assert subtract_7346(10, 4) == 6

def test_multiply_7347():
    assert multiply_7347(3, 7) == 21

def test_divide_7348():
    assert divide_7348(10, 2) == 5.0
