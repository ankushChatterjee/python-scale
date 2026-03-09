"""Tests for test module 1191 — covers src modules [4761, 4762, 4763, 4764]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4761 import add_4761
from module_4762 import subtract_4762
from module_4763 import multiply_4763
from module_4764 import divide_4764

def test_add_4761():
    assert add_4761(2, 3) == 5

def test_subtract_4762():
    assert subtract_4762(10, 4) == 6

def test_multiply_4763():
    assert multiply_4763(3, 7) == 21

def test_divide_4764():
    assert divide_4764(10, 2) == 5.0
