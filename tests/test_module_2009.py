"""Tests for test module 2009 — covers src modules [8033, 8034, 8035, 8036]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8033 import add_8033
from module_8034 import subtract_8034
from module_8035 import multiply_8035
from module_8036 import divide_8036

def test_add_8033():
    assert add_8033(2, 3) == 5

def test_subtract_8034():
    assert subtract_8034(10, 4) == 6

def test_multiply_8035():
    assert multiply_8035(3, 7) == 21

def test_divide_8036():
    assert divide_8036(10, 2) == 5.0
