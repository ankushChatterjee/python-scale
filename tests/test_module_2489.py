"""Tests for test module 2489 — covers src modules [9953, 9954, 9955, 9956]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9953 import add_9953
from module_9954 import subtract_9954
from module_9955 import multiply_9955
from module_9956 import divide_9956

def test_add_9953():
    assert add_9953(2, 3) == 5

def test_subtract_9954():
    assert subtract_9954(10, 4) == 6

def test_multiply_9955():
    assert multiply_9955(3, 7) == 21

def test_divide_9956():
    assert divide_9956(10, 2) == 5.0
