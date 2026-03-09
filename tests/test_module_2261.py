"""Tests for test module 2261 — covers src modules [9041, 9042, 9043, 9044]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9041 import add_9041
from module_9042 import subtract_9042
from module_9043 import multiply_9043
from module_9044 import divide_9044

def test_add_9041():
    assert add_9041(2, 3) == 5

def test_subtract_9042():
    assert subtract_9042(10, 4) == 6

def test_multiply_9043():
    assert multiply_9043(3, 7) == 21

def test_divide_9044():
    assert divide_9044(10, 2) == 5.0
