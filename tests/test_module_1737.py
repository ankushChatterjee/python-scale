"""Tests for test module 1737 — covers src modules [6945, 6946, 6947, 6948]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6945 import add_6945
from module_6946 import subtract_6946
from module_6947 import multiply_6947
from module_6948 import divide_6948

def test_add_6945():
    assert add_6945(2, 3) == 5

def test_subtract_6946():
    assert subtract_6946(10, 4) == 6

def test_multiply_6947():
    assert multiply_6947(3, 7) == 21

def test_divide_6948():
    assert divide_6948(10, 2) == 5.0
