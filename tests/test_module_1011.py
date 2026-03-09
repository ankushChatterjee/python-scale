"""Tests for test module 1011 — covers src modules [4041, 4042, 4043, 4044]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4041 import add_4041
from module_4042 import subtract_4042
from module_4043 import multiply_4043
from module_4044 import divide_4044

def test_add_4041():
    assert add_4041(2, 3) == 5

def test_subtract_4042():
    assert subtract_4042(10, 4) == 6

def test_multiply_4043():
    assert multiply_4043(3, 7) == 21

def test_divide_4044():
    assert divide_4044(10, 2) == 5.0
