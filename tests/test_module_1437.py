"""Tests for test module 1437 — covers src modules [5745, 5746, 5747, 5748]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5745 import add_5745
from module_5746 import subtract_5746
from module_5747 import multiply_5747
from module_5748 import divide_5748

def test_add_5745():
    assert add_5745(2, 3) == 5

def test_subtract_5746():
    assert subtract_5746(10, 4) == 6

def test_multiply_5747():
    assert multiply_5747(3, 7) == 21

def test_divide_5748():
    assert divide_5748(10, 2) == 5.0
