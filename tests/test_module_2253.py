"""Tests for test module 2253 — covers src modules [9009, 9010, 9011, 9012]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9009 import add_9009
from module_9010 import subtract_9010
from module_9011 import multiply_9011
from module_9012 import divide_9012

def test_add_9009():
    assert add_9009(2, 3) == 5

def test_subtract_9010():
    assert subtract_9010(10, 4) == 6

def test_multiply_9011():
    assert multiply_9011(3, 7) == 21

def test_divide_9012():
    assert divide_9012(10, 2) == 5.0
