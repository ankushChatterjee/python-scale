"""Tests for test module 1261 — covers src modules [5041, 5042, 5043, 5044]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5041 import add_5041
from module_5042 import subtract_5042
from module_5043 import multiply_5043
from module_5044 import divide_5044

def test_add_5041():
    assert add_5041(2, 3) == 5

def test_subtract_5042():
    assert subtract_5042(10, 4) == 6

def test_multiply_5043():
    assert multiply_5043(3, 7) == 21

def test_divide_5044():
    assert divide_5044(10, 2) == 5.0
