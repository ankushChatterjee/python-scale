"""Tests for test module 1001 — covers src modules [4001, 4002, 4003, 4004]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4001 import add_4001
from module_4002 import subtract_4002
from module_4003 import multiply_4003
from module_4004 import divide_4004

def test_add_4001():
    assert add_4001(2, 3) == 5

def test_subtract_4002():
    assert subtract_4002(10, 4) == 6

def test_multiply_4003():
    assert multiply_4003(3, 7) == 21

def test_divide_4004():
    assert divide_4004(10, 2) == 5.0
