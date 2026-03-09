"""Tests for test module 1507 — covers src modules [6025, 6026, 6027, 6028]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6025 import add_6025
from module_6026 import subtract_6026
from module_6027 import multiply_6027
from module_6028 import divide_6028

def test_add_6025():
    assert add_6025(2, 3) == 5

def test_subtract_6026():
    assert subtract_6026(10, 4) == 6

def test_multiply_6027():
    assert multiply_6027(3, 7) == 21

def test_divide_6028():
    assert divide_6028(10, 2) == 5.0
