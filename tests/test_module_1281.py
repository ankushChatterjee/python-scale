"""Tests for test module 1281 — covers src modules [5121, 5122, 5123, 5124]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5121 import add_5121
from module_5122 import subtract_5122
from module_5123 import multiply_5123
from module_5124 import divide_5124

def test_add_5121():
    assert add_5121(2, 3) == 5

def test_subtract_5122():
    assert subtract_5122(10, 4) == 6

def test_multiply_5123():
    assert multiply_5123(3, 7) == 21

def test_divide_5124():
    assert divide_5124(10, 2) == 5.0
