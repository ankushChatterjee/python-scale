"""Tests for test module 2497 — covers src modules [9985, 9986, 9987, 9988]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9985 import add_9985
from module_9986 import subtract_9986
from module_9987 import multiply_9987
from module_9988 import divide_9988

def test_add_9985():
    assert add_9985(2, 3) == 5

def test_subtract_9986():
    assert subtract_9986(10, 4) == 6

def test_multiply_9987():
    assert multiply_9987(3, 7) == 21

def test_divide_9988():
    assert divide_9988(10, 2) == 5.0
