"""Tests for test module 649 — covers src modules [2593, 2594, 2595, 2596]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2593 import add_2593
from module_2594 import subtract_2594
from module_2595 import multiply_2595
from module_2596 import divide_2596

def test_add_2593():
    assert add_2593(2, 3) == 5

def test_subtract_2594():
    assert subtract_2594(10, 4) == 6

def test_multiply_2595():
    assert multiply_2595(3, 7) == 21

def test_divide_2596():
    assert divide_2596(10, 2) == 5.0
