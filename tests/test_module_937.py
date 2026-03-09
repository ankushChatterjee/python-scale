"""Tests for test module 937 — covers src modules [3745, 3746, 3747, 3748]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3745 import add_3745
from module_3746 import subtract_3746
from module_3747 import multiply_3747
from module_3748 import divide_3748

def test_add_3745():
    assert add_3745(2, 3) == 5

def test_subtract_3746():
    assert subtract_3746(10, 4) == 6

def test_multiply_3747():
    assert multiply_3747(3, 7) == 21

def test_divide_3748():
    assert divide_3748(10, 2) == 5.0
