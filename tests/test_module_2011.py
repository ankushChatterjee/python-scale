"""Tests for test module 2011 — covers src modules [8041, 8042, 8043, 8044]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8041 import add_8041
from module_8042 import subtract_8042
from module_8043 import multiply_8043
from module_8044 import divide_8044

def test_add_8041():
    assert add_8041(2, 3) == 5

def test_subtract_8042():
    assert subtract_8042(10, 4) == 6

def test_multiply_8043():
    assert multiply_8043(3, 7) == 21

def test_divide_8044():
    assert divide_8044(10, 2) == 5.0
