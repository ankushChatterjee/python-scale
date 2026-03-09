"""Tests for test module 2441 — covers src modules [9761, 9762, 9763, 9764]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9761 import add_9761
from module_9762 import subtract_9762
from module_9763 import multiply_9763
from module_9764 import divide_9764

def test_add_9761():
    assert add_9761(2, 3) == 5

def test_subtract_9762():
    assert subtract_9762(10, 4) == 6

def test_multiply_9763():
    assert multiply_9763(3, 7) == 21

def test_divide_9764():
    assert divide_9764(10, 2) == 5.0
