"""Tests for test module 921 — covers src modules [3681, 3682, 3683, 3684]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3681 import add_3681
from module_3682 import subtract_3682
from module_3683 import multiply_3683
from module_3684 import divide_3684

def test_add_3681():
    assert add_3681(2, 3) == 5

def test_subtract_3682():
    assert subtract_3682(10, 4) == 6

def test_multiply_3683():
    assert multiply_3683(3, 7) == 21

def test_divide_3684():
    assert divide_3684(10, 2) == 5.0
