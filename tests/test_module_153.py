"""Tests for test module 153 — covers src modules [609, 610, 611, 612]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_609 import add_609
from module_610 import subtract_610
from module_611 import multiply_611
from module_612 import divide_612

def test_add_609():
    assert add_609(2, 3) == 5

def test_subtract_610():
    assert subtract_610(10, 4) == 6

def test_multiply_611():
    assert multiply_611(3, 7) == 21

def test_divide_612():
    assert divide_612(10, 2) == 5.0
