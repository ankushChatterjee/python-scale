"""Tests for test module 2397 — covers src modules [9585, 9586, 9587, 9588]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9585 import add_9585
from module_9586 import subtract_9586
from module_9587 import multiply_9587
from module_9588 import divide_9588

def test_add_9585():
    assert add_9585(2, 3) == 5

def test_subtract_9586():
    assert subtract_9586(10, 4) == 6

def test_multiply_9587():
    assert multiply_9587(3, 7) == 21

def test_divide_9588():
    assert divide_9588(10, 2) == 5.0
