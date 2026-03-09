"""Tests for test module 1187 — covers src modules [4745, 4746, 4747, 4748]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4745 import add_4745
from module_4746 import subtract_4746
from module_4747 import multiply_4747
from module_4748 import divide_4748

def test_add_4745():
    assert add_4745(2, 3) == 5

def test_subtract_4746():
    assert subtract_4746(10, 4) == 6

def test_multiply_4747():
    assert multiply_4747(3, 7) == 21

def test_divide_4748():
    assert divide_4748(10, 2) == 5.0
