"""Tests for test module 1237 — covers src modules [4945, 4946, 4947, 4948]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4945 import add_4945
from module_4946 import subtract_4946
from module_4947 import multiply_4947
from module_4948 import divide_4948

def test_add_4945():
    assert add_4945(2, 3) == 5

def test_subtract_4946():
    assert subtract_4946(10, 4) == 6

def test_multiply_4947():
    assert multiply_4947(3, 7) == 21

def test_divide_4948():
    assert divide_4948(10, 2) == 5.0
