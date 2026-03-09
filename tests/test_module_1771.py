"""Tests for test module 1771 — covers src modules [7081, 7082, 7083, 7084]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7081 import add_7081
from module_7082 import subtract_7082
from module_7083 import multiply_7083
from module_7084 import divide_7084

def test_add_7081():
    assert add_7081(2, 3) == 5

def test_subtract_7082():
    assert subtract_7082(10, 4) == 6

def test_multiply_7083():
    assert multiply_7083(3, 7) == 21

def test_divide_7084():
    assert divide_7084(10, 2) == 5.0
