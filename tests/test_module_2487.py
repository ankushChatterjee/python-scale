"""Tests for test module 2487 — covers src modules [9945, 9946, 9947, 9948]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9945 import add_9945
from module_9946 import subtract_9946
from module_9947 import multiply_9947
from module_9948 import divide_9948

def test_add_9945():
    assert add_9945(2, 3) == 5

def test_subtract_9946():
    assert subtract_9946(10, 4) == 6

def test_multiply_9947():
    assert multiply_9947(3, 7) == 21

def test_divide_9948():
    assert divide_9948(10, 2) == 5.0
