"""Tests for test module 1253 — covers src modules [5009, 5010, 5011, 5012]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5009 import add_5009
from module_5010 import subtract_5010
from module_5011 import multiply_5011
from module_5012 import divide_5012

def test_add_5009():
    assert add_5009(2, 3) == 5

def test_subtract_5010():
    assert subtract_5010(10, 4) == 6

def test_multiply_5011():
    assert multiply_5011(3, 7) == 21

def test_divide_5012():
    assert divide_5012(10, 2) == 5.0
