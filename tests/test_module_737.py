"""Tests for test module 737 — covers src modules [2945, 2946, 2947, 2948]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2945 import add_2945
from module_2946 import subtract_2946
from module_2947 import multiply_2947
from module_2948 import divide_2948

def test_add_2945():
    assert add_2945(2, 3) == 5

def test_subtract_2946():
    assert subtract_2946(10, 4) == 6

def test_multiply_2947():
    assert multiply_2947(3, 7) == 21

def test_divide_2948():
    assert divide_2948(10, 2) == 5.0
