"""Tests for test module 1671 — covers src modules [6681, 6682, 6683, 6684]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6681 import add_6681
from module_6682 import subtract_6682
from module_6683 import multiply_6683
from module_6684 import divide_6684

def test_add_6681():
    assert add_6681(2, 3) == 5

def test_subtract_6682():
    assert subtract_6682(10, 4) == 6

def test_multiply_6683():
    assert multiply_6683(3, 7) == 21

def test_divide_6684():
    assert divide_6684(10, 2) == 5.0
