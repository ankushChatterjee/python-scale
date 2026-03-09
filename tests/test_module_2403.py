"""Tests for test module 2403 — covers src modules [9609, 9610, 9611, 9612]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9609 import add_9609
from module_9610 import subtract_9610
from module_9611 import multiply_9611
from module_9612 import divide_9612

def test_add_9609():
    assert add_9609(2, 3) == 5

def test_subtract_9610():
    assert subtract_9610(10, 4) == 6

def test_multiply_9611():
    assert multiply_9611(3, 7) == 21

def test_divide_9612():
    assert divide_9612(10, 2) == 5.0
