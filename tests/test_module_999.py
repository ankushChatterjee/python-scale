"""Tests for test module 999 — covers src modules [3993, 3994, 3995, 3996]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3993 import add_3993
from module_3994 import subtract_3994
from module_3995 import multiply_3995
from module_3996 import divide_3996

def test_add_3993():
    assert add_3993(2, 3) == 5

def test_subtract_3994():
    assert subtract_3994(10, 4) == 6

def test_multiply_3995():
    assert multiply_3995(3, 7) == 21

def test_divide_3996():
    assert divide_3996(10, 2) == 5.0
