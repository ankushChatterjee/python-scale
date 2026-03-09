"""Tests for test module 1031 — covers src modules [4121, 4122, 4123, 4124]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4121 import add_4121
from module_4122 import subtract_4122
from module_4123 import multiply_4123
from module_4124 import divide_4124

def test_add_4121():
    assert add_4121(2, 3) == 5

def test_subtract_4122():
    assert subtract_4122(10, 4) == 6

def test_multiply_4123():
    assert multiply_4123(3, 7) == 21

def test_divide_4124():
    assert divide_4124(10, 2) == 5.0
