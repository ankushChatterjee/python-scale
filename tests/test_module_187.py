"""Tests for test module 187 — covers src modules [745, 746, 747, 748]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_745 import add_745
from module_746 import subtract_746
from module_747 import multiply_747
from module_748 import divide_748

def test_add_745():
    assert add_745(2, 3) == 5

def test_subtract_746():
    assert subtract_746(10, 4) == 6

def test_multiply_747():
    assert multiply_747(3, 7) == 21

def test_divide_748():
    assert divide_748(10, 2) == 5.0
