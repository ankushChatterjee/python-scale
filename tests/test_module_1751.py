"""Tests for test module 1751 — covers src modules [7001, 7002, 7003, 7004]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7001 import add_7001
from module_7002 import subtract_7002
from module_7003 import multiply_7003
from module_7004 import divide_7004

def test_add_7001():
    assert add_7001(2, 3) == 5

def test_subtract_7002():
    assert subtract_7002(10, 4) == 6

def test_multiply_7003():
    assert multiply_7003(3, 7) == 21

def test_divide_7004():
    assert divide_7004(10, 2) == 5.0
