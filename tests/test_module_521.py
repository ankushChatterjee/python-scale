"""Tests for test module 521 — covers src modules [2081, 2082, 2083, 2084]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2081 import add_2081
from module_2082 import subtract_2082
from module_2083 import multiply_2083
from module_2084 import divide_2084

def test_add_2081():
    assert add_2081(2, 3) == 5

def test_subtract_2082():
    assert subtract_2082(10, 4) == 6

def test_multiply_2083():
    assert multiply_2083(3, 7) == 21

def test_divide_2084():
    assert divide_2084(10, 2) == 5.0
