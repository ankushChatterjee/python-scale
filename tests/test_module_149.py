"""Tests for test module 149 — covers src modules [593, 594, 595, 596]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_593 import add_593
from module_594 import subtract_594
from module_595 import multiply_595
from module_596 import divide_596

def test_add_593():
    assert add_593(2, 3) == 5

def test_subtract_594():
    assert subtract_594(10, 4) == 6

def test_multiply_595():
    assert multiply_595(3, 7) == 21

def test_divide_596():
    assert divide_596(10, 2) == 5.0
