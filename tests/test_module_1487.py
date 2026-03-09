"""Tests for test module 1487 — covers src modules [5945, 5946, 5947, 5948]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5945 import add_5945
from module_5946 import subtract_5946
from module_5947 import multiply_5947
from module_5948 import divide_5948

def test_add_5945():
    assert add_5945(2, 3) == 5

def test_subtract_5946():
    assert subtract_5946(10, 4) == 6

def test_multiply_5947():
    assert multiply_5947(3, 7) == 21

def test_divide_5948():
    assert divide_5948(10, 2) == 5.0
