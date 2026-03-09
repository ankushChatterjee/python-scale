"""Tests for test module 503 — covers src modules [2009, 2010, 2011, 2012]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2009 import add_2009
from module_2010 import subtract_2010
from module_2011 import multiply_2011
from module_2012 import divide_2012

def test_add_2009():
    assert add_2009(2, 3) == 5

def test_subtract_2010():
    assert subtract_2010(10, 4) == 6

def test_multiply_2011():
    assert multiply_2011(3, 7) == 21

def test_divide_2012():
    assert divide_2012(10, 2) == 5.0
