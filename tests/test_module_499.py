"""Tests for test module 499 — covers src modules [1993, 1994, 1995, 1996]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1993 import add_1993
from module_1994 import subtract_1994
from module_1995 import multiply_1995
from module_1996 import divide_1996

def test_add_1993():
    assert add_1993(2, 3) == 5

def test_subtract_1994():
    assert subtract_1994(10, 4) == 6

def test_multiply_1995():
    assert multiply_1995(3, 7) == 21

def test_divide_1996():
    assert divide_1996(10, 2) == 5.0
