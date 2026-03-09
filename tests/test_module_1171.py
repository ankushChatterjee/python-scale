"""Tests for test module 1171 — covers src modules [4681, 4682, 4683, 4684]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4681 import add_4681
from module_4682 import subtract_4682
from module_4683 import multiply_4683
from module_4684 import divide_4684

def test_add_4681():
    assert add_4681(2, 3) == 5

def test_subtract_4682():
    assert subtract_4682(10, 4) == 6

def test_multiply_4683():
    assert multiply_4683(3, 7) == 21

def test_divide_4684():
    assert divide_4684(10, 2) == 5.0
