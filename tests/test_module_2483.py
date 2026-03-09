"""Tests for test module 2483 — covers src modules [9929, 9930, 9931, 9932]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9929 import add_9929
from module_9930 import subtract_9930
from module_9931 import multiply_9931
from module_9932 import divide_9932

def test_add_9929():
    assert add_9929(2, 3) == 5

def test_subtract_9930():
    assert subtract_9930(10, 4) == 6

def test_multiply_9931():
    assert multiply_9931(3, 7) == 21

def test_divide_9932():
    assert divide_9932(10, 2) == 5.0
