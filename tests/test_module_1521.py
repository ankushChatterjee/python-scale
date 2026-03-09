"""Tests for test module 1521 — covers src modules [6081, 6082, 6083, 6084]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6081 import add_6081
from module_6082 import subtract_6082
from module_6083 import multiply_6083
from module_6084 import divide_6084

def test_add_6081():
    assert add_6081(2, 3) == 5

def test_subtract_6082():
    assert subtract_6082(10, 4) == 6

def test_multiply_6083():
    assert multiply_6083(3, 7) == 21

def test_divide_6084():
    assert divide_6084(10, 2) == 5.0
