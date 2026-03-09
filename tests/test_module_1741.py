"""Tests for test module 1741 — covers src modules [6961, 6962, 6963, 6964]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6961 import add_6961
from module_6962 import subtract_6962
from module_6963 import multiply_6963
from module_6964 import divide_6964

def test_add_6961():
    assert add_6961(2, 3) == 5

def test_subtract_6962():
    assert subtract_6962(10, 4) == 6

def test_multiply_6963():
    assert multiply_6963(3, 7) == 21

def test_divide_6964():
    assert divide_6964(10, 2) == 5.0
