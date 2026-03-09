"""Tests for test module 1251 — covers src modules [5001, 5002, 5003, 5004]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5001 import add_5001
from module_5002 import subtract_5002
from module_5003 import multiply_5003
from module_5004 import divide_5004

def test_add_5001():
    assert add_5001(2, 3) == 5

def test_subtract_5002():
    assert subtract_5002(10, 4) == 6

def test_multiply_5003():
    assert multiply_5003(3, 7) == 21

def test_divide_5004():
    assert divide_5004(10, 2) == 5.0
