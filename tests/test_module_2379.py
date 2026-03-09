"""Tests for test module 2379 — covers src modules [9513, 9514, 9515, 9516]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9513 import add_9513
from module_9514 import subtract_9514
from module_9515 import multiply_9515
from module_9516 import divide_9516

def test_add_9513():
    assert add_9513(2, 3) == 5

def test_subtract_9514():
    assert subtract_9514(10, 4) == 6

def test_multiply_9515():
    assert multiply_9515(3, 7) == 21

def test_divide_9516():
    assert divide_9516(10, 2) == 5.0
