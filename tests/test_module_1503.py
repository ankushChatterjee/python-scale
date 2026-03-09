"""Tests for test module 1503 — covers src modules [6009, 6010, 6011, 6012]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6009 import add_6009
from module_6010 import subtract_6010
from module_6011 import multiply_6011
from module_6012 import divide_6012

def test_add_6009():
    assert add_6009(2, 3) == 5

def test_subtract_6010():
    assert subtract_6010(10, 4) == 6

def test_multiply_6011():
    assert multiply_6011(3, 7) == 21

def test_divide_6012():
    assert divide_6012(10, 2) == 5.0
