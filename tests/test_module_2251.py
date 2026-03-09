"""Tests for test module 2251 — covers src modules [9001, 9002, 9003, 9004]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9001 import add_9001
from module_9002 import subtract_9002
from module_9003 import multiply_9003
from module_9004 import divide_9004

def test_add_9001():
    assert add_9001(2, 3) == 5

def test_subtract_9002():
    assert subtract_9002(10, 4) == 6

def test_multiply_9003():
    assert multiply_9003(3, 7) == 21

def test_divide_9004():
    assert divide_9004(10, 2) == 5.0
