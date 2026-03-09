"""Tests for test module 1149 — covers src modules [4593, 4594, 4595, 4596]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4593 import add_4593
from module_4594 import subtract_4594
from module_4595 import multiply_4595
from module_4596 import divide_4596

def test_add_4593():
    assert add_4593(2, 3) == 5

def test_subtract_4594():
    assert subtract_4594(10, 4) == 6

def test_multiply_4595():
    assert multiply_4595(3, 7) == 21

def test_divide_4596():
    assert divide_4596(10, 2) == 5.0
