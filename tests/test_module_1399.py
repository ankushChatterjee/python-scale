"""Tests for test module 1399 — covers src modules [5593, 5594, 5595, 5596]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5593 import add_5593
from module_5594 import subtract_5594
from module_5595 import multiply_5595
from module_5596 import divide_5596

def test_add_5593():
    assert add_5593(2, 3) == 5

def test_subtract_5594():
    assert subtract_5594(10, 4) == 6

def test_multiply_5595():
    assert multiply_5595(3, 7) == 21

def test_divide_5596():
    assert divide_5596(10, 2) == 5.0
