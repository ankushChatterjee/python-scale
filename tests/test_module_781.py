"""Tests for test module 781 — covers src modules [3121, 3122, 3123, 3124]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3121 import add_3121
from module_3122 import subtract_3122
from module_3123 import multiply_3123
from module_3124 import divide_3124

def test_add_3121():
    assert add_3121(2, 3) == 5

def test_subtract_3122():
    assert subtract_3122(10, 4) == 6

def test_multiply_3123():
    assert multiply_3123(3, 7) == 21

def test_divide_3124():
    assert divide_3124(10, 2) == 5.0
