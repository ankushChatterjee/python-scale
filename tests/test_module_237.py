"""Tests for test module 237 — covers src modules [945, 946, 947, 948]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_945 import add_945
from module_946 import subtract_946
from module_947 import multiply_947
from module_948 import divide_948

def test_add_945():
    assert add_945(2, 3) == 5

def test_subtract_946():
    assert subtract_946(10, 4) == 6

def test_multiply_947():
    assert multiply_947(3, 7) == 21

def test_divide_948():
    assert divide_948(10, 2) == 5.0
