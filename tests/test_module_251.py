"""Tests for test module 251 — covers src modules [1001, 1002, 1003, 1004]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1001 import add_1001
from module_1002 import subtract_1002
from module_1003 import multiply_1003
from module_1004 import divide_1004

def test_add_1001():
    assert add_1001(2, 3) == 5

def test_subtract_1002():
    assert subtract_1002(10, 4) == 6

def test_multiply_1003():
    assert multiply_1003(3, 7) == 21

def test_divide_1004():
    assert divide_1004(10, 2) == 5.0
