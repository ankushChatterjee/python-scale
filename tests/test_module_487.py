"""Tests for test module 487 — covers src modules [1945, 1946, 1947, 1948]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1945 import add_1945
from module_1946 import subtract_1946
from module_1947 import multiply_1947
from module_1948 import divide_1948

def test_add_1945():
    assert add_1945(2, 3) == 5

def test_subtract_1946():
    assert subtract_1946(10, 4) == 6

def test_multiply_1947():
    assert multiply_1947(3, 7) == 21

def test_divide_1948():
    assert divide_1948(10, 2) == 5.0
