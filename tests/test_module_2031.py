"""Tests for test module 2031 — covers src modules [8121, 8122, 8123, 8124]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8121 import add_8121
from module_8122 import subtract_8122
from module_8123 import multiply_8123
from module_8124 import divide_8124

def test_add_8121():
    assert add_8121(2, 3) == 5

def test_subtract_8122():
    assert subtract_8122(10, 4) == 6

def test_multiply_8123():
    assert multiply_8123(3, 7) == 21

def test_divide_8124():
    assert divide_8124(10, 2) == 5.0
