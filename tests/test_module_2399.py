"""Tests for test module 2399 — covers src modules [9593, 9594, 9595, 9596]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9593 import add_9593
from module_9594 import subtract_9594
from module_9595 import multiply_9595
from module_9596 import divide_9596

def test_add_9593():
    assert add_9593(2, 3) == 5

def test_subtract_9594():
    assert subtract_9594(10, 4) == 6

def test_multiply_9595():
    assert multiply_9595(3, 7) == 21

def test_divide_9596():
    assert divide_9596(10, 2) == 5.0
