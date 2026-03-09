"""Tests for test module 2149 — covers src modules [8593, 8594, 8595, 8596]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8593 import add_8593
from module_8594 import subtract_8594
from module_8595 import multiply_8595
from module_8596 import divide_8596

def test_add_8593():
    assert add_8593(2, 3) == 5

def test_subtract_8594():
    assert subtract_8594(10, 4) == 6

def test_multiply_8595():
    assert multiply_8595(3, 7) == 21

def test_divide_8596():
    assert divide_8596(10, 2) == 5.0
