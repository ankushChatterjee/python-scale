"""Tests for test module 751 — covers src modules [3001, 3002, 3003, 3004]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3001 import add_3001
from module_3002 import subtract_3002
from module_3003 import multiply_3003
from module_3004 import divide_3004

def test_add_3001():
    assert add_3001(2, 3) == 5

def test_subtract_3002():
    assert subtract_3002(10, 4) == 6

def test_multiply_3003():
    assert multiply_3003(3, 7) == 21

def test_divide_3004():
    assert divide_3004(10, 2) == 5.0
