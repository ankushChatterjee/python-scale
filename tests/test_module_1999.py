"""Tests for test module 1999 — covers src modules [7993, 7994, 7995, 7996]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7993 import add_7993
from module_7994 import subtract_7994
from module_7995 import multiply_7995
from module_7996 import divide_7996

def test_add_7993():
    assert add_7993(2, 3) == 5

def test_subtract_7994():
    assert subtract_7994(10, 4) == 6

def test_multiply_7995():
    assert multiply_7995(3, 7) == 21

def test_divide_7996():
    assert divide_7996(10, 2) == 5.0
