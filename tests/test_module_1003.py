"""Tests for test module 1003 — covers src modules [4009, 4010, 4011, 4012]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4009 import add_4009
from module_4010 import subtract_4010
from module_4011 import multiply_4011
from module_4012 import divide_4012

def test_add_4009():
    assert add_4009(2, 3) == 5

def test_subtract_4010():
    assert subtract_4010(10, 4) == 6

def test_multiply_4011():
    assert multiply_4011(3, 7) == 21

def test_divide_4012():
    assert divide_4012(10, 2) == 5.0
