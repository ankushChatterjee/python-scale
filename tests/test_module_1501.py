"""Tests for test module 1501 — covers src modules [6001, 6002, 6003, 6004]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6001 import add_6001
from module_6002 import subtract_6002
from module_6003 import multiply_6003
from module_6004 import divide_6004

def test_add_6001():
    assert add_6001(2, 3) == 5

def test_subtract_6002():
    assert subtract_6002(10, 4) == 6

def test_multiply_6003():
    assert multiply_6003(3, 7) == 21

def test_divide_6004():
    assert divide_6004(10, 2) == 5.0
