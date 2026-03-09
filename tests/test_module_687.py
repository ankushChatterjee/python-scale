"""Tests for test module 687 — covers src modules [2745, 2746, 2747, 2748]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2745 import add_2745
from module_2746 import subtract_2746
from module_2747 import multiply_2747
from module_2748 import divide_2748

def test_add_2745():
    assert add_2745(2, 3) == 5

def test_subtract_2746():
    assert subtract_2746(10, 4) == 6

def test_multiply_2747():
    assert multiply_2747(3, 7) == 21

def test_divide_2748():
    assert divide_2748(10, 2) == 5.0
