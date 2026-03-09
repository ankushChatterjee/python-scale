"""Tests for test module 653 — covers src modules [2609, 2610, 2611, 2612]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2609 import add_2609
from module_2610 import subtract_2610
from module_2611 import multiply_2611
from module_2612 import divide_2612

def test_add_2609():
    assert add_2609(2, 3) == 5

def test_subtract_2610():
    assert subtract_2610(10, 4) == 6

def test_multiply_2611():
    assert multiply_2611(3, 7) == 21

def test_divide_2612():
    assert divide_2612(10, 2) == 5.0
