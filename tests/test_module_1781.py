"""Tests for test module 1781 — covers src modules [7121, 7122, 7123, 7124]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7121 import add_7121
from module_7122 import subtract_7122
from module_7123 import multiply_7123
from module_7124 import divide_7124

def test_add_7121():
    assert add_7121(2, 3) == 5

def test_subtract_7122():
    assert subtract_7122(10, 4) == 6

def test_multiply_7123():
    assert multiply_7123(3, 7) == 21

def test_divide_7124():
    assert divide_7124(10, 2) == 5.0
