"""Tests for test module 281 — covers src modules [1121, 1122, 1123, 1124]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1121 import add_1121
from module_1122 import subtract_1122
from module_1123 import multiply_1123
from module_1124 import divide_1124

def test_add_1121():
    assert add_1121(2, 3) == 5

def test_subtract_1122():
    assert subtract_1122(10, 4) == 6

def test_multiply_1123():
    assert multiply_1123(3, 7) == 21

def test_divide_1124():
    assert divide_1124(10, 2) == 5.0
