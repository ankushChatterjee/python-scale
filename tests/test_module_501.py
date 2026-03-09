"""Tests for test module 501 — covers src modules [2001, 2002, 2003, 2004]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2001 import add_2001
from module_2002 import subtract_2002
from module_2003 import multiply_2003
from module_2004 import divide_2004

def test_add_2001():
    assert add_2001(2, 3) == 5

def test_subtract_2002():
    assert subtract_2002(10, 4) == 6

def test_multiply_2003():
    assert multiply_2003(3, 7) == 21

def test_divide_2004():
    assert divide_2004(10, 2) == 5.0
