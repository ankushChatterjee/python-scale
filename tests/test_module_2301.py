"""Tests for test module 2301 — covers src modules [9201, 9202, 9203, 9204]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9201 import add_9201
from module_9202 import subtract_9202
from module_9203 import multiply_9203
from module_9204 import divide_9204

def test_add_9201():
    assert add_9201(2, 3) == 5

def test_subtract_9202():
    assert subtract_9202(10, 4) == 6

def test_multiply_9203():
    assert multiply_9203(3, 7) == 21

def test_divide_9204():
    assert divide_9204(10, 2) == 5.0
