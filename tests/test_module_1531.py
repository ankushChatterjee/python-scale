"""Tests for test module 1531 — covers src modules [6121, 6122, 6123, 6124]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6121 import add_6121
from module_6122 import subtract_6122
from module_6123 import multiply_6123
from module_6124 import divide_6124

def test_add_6121():
    assert add_6121(2, 3) == 5

def test_subtract_6122():
    assert subtract_6122(10, 4) == 6

def test_multiply_6123():
    assert multiply_6123(3, 7) == 21

def test_divide_6124():
    assert divide_6124(10, 2) == 5.0
