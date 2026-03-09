"""Tests for test module 2437 — covers src modules [9745, 9746, 9747, 9748]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9745 import add_9745
from module_9746 import subtract_9746
from module_9747 import multiply_9747
from module_9748 import divide_9748

def test_add_9745():
    assert add_9745(2, 3) == 5

def test_subtract_9746():
    assert subtract_9746(10, 4) == 6

def test_multiply_9747():
    assert multiply_9747(3, 7) == 21

def test_divide_9748():
    assert divide_9748(10, 2) == 5.0
