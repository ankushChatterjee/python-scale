"""Tests for test module 2001 — covers src modules [8001, 8002, 8003, 8004]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8001 import add_8001
from module_8002 import subtract_8002
from module_8003 import multiply_8003
from module_8004 import divide_8004

def test_add_8001():
    assert add_8001(2, 3) == 5

def test_subtract_8002():
    assert subtract_8002(10, 4) == 6

def test_multiply_8003():
    assert multiply_8003(3, 7) == 21

def test_divide_8004():
    assert divide_8004(10, 2) == 5.0
