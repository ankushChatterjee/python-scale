"""Tests for test module 1021 — covers src modules [4081, 4082, 4083, 4084]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4081 import add_4081
from module_4082 import subtract_4082
from module_4083 import multiply_4083
from module_4084 import divide_4084

def test_add_4081():
    assert add_4081(2, 3) == 5

def test_subtract_4082():
    assert subtract_4082(10, 4) == 6

def test_multiply_4083():
    assert multiply_4083(3, 7) == 21

def test_divide_4084():
    assert divide_4084(10, 2) == 5.0
