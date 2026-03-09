"""Tests for test module 1009 — covers src modules [4033, 4034, 4035, 4036]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4033 import add_4033
from module_4034 import subtract_4034
from module_4035 import multiply_4035
from module_4036 import divide_4036

def test_add_4033():
    assert add_4033(2, 3) == 5

def test_subtract_4034():
    assert subtract_4034(10, 4) == 6

def test_multiply_4035():
    assert multiply_4035(3, 7) == 21

def test_divide_4036():
    assert divide_4036(10, 2) == 5.0
