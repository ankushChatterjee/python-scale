"""Tests for test module 1259 — covers src modules [5033, 5034, 5035, 5036]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5033 import add_5033
from module_5034 import subtract_5034
from module_5035 import multiply_5035
from module_5036 import divide_5036

def test_add_5033():
    assert add_5033(2, 3) == 5

def test_subtract_5034():
    assert subtract_5034(10, 4) == 6

def test_multiply_5035():
    assert multiply_5035(3, 7) == 21

def test_divide_5036():
    assert divide_5036(10, 2) == 5.0
