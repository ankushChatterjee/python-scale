"""Tests for test module 31 — covers src modules [121, 122, 123, 124]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_121 import add_121
from module_122 import subtract_122
from module_123 import multiply_123
from module_124 import divide_124

def test_add_121():
    assert add_121(2, 3) == 5

def test_subtract_122():
    assert subtract_122(10, 4) == 6

def test_multiply_123():
    assert multiply_123(3, 7) == 21

def test_divide_124():
    assert divide_124(10, 2) == 5.0
