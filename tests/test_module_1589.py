"""Tests for test module 1589 — covers src modules [6353, 6354, 6355, 6356]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6353 import add_6353
from module_6354 import subtract_6354
from module_6355 import multiply_6355
from module_6356 import divide_6356

def test_add_6353():
    assert add_6353(2, 3) == 5

def test_subtract_6354():
    assert subtract_6354(10, 4) == 6

def test_multiply_6355():
    assert multiply_6355(3, 7) == 21

def test_divide_6356():
    assert divide_6356(10, 2) == 5.0
