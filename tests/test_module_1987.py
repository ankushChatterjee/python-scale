"""Tests for test module 1987 — covers src modules [7945, 7946, 7947, 7948]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7945 import add_7945
from module_7946 import subtract_7946
from module_7947 import multiply_7947
from module_7948 import divide_7948

def test_add_7945():
    assert add_7945(2, 3) == 5

def test_subtract_7946():
    assert subtract_7946(10, 4) == 6

def test_multiply_7947():
    assert multiply_7947(3, 7) == 21

def test_divide_7948():
    assert divide_7948(10, 2) == 5.0
