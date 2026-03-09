"""Tests for test module 987 — covers src modules [3945, 3946, 3947, 3948]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3945 import add_3945
from module_3946 import subtract_3946
from module_3947 import multiply_3947
from module_3948 import divide_3948

def test_add_3945():
    assert add_3945(2, 3) == 5

def test_subtract_3946():
    assert subtract_3946(10, 4) == 6

def test_multiply_3947():
    assert multiply_3947(3, 7) == 21

def test_divide_3948():
    assert divide_3948(10, 2) == 5.0
