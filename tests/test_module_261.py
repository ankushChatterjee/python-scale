"""Tests for test module 261 — covers src modules [1041, 1042, 1043, 1044]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1041 import add_1041
from module_1042 import subtract_1042
from module_1043 import multiply_1043
from module_1044 import divide_1044

def test_add_1041():
    assert add_1041(2, 3) == 5

def test_subtract_1042():
    assert subtract_1042(10, 4) == 6

def test_multiply_1043():
    assert multiply_1043(3, 7) == 21

def test_divide_1044():
    assert divide_1044(10, 2) == 5.0
