"""Tests for test module 2381 — covers src modules [9521, 9522, 9523, 9524]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9521 import add_9521
from module_9522 import subtract_9522
from module_9523 import multiply_9523
from module_9524 import divide_9524

def test_add_9521():
    assert add_9521(2, 3) == 5

def test_subtract_9522():
    assert subtract_9522(10, 4) == 6

def test_multiply_9523():
    assert multiply_9523(3, 7) == 21

def test_divide_9524():
    assert divide_9524(10, 2) == 5.0
