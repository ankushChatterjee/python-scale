"""Tests for test module 2427 — covers src modules [9705, 9706, 9707, 9708]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9705 import add_9705
from module_9706 import subtract_9706
from module_9707 import multiply_9707
from module_9708 import divide_9708

def test_add_9705():
    assert add_9705(2, 3) == 5

def test_subtract_9706():
    assert subtract_9706(10, 4) == 6

def test_multiply_9707():
    assert multiply_9707(3, 7) == 21

def test_divide_9708():
    assert divide_9708(10, 2) == 5.0
