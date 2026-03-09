"""Tests for test module 1499 — covers src modules [5993, 5994, 5995, 5996]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5993 import add_5993
from module_5994 import subtract_5994
from module_5995 import multiply_5995
from module_5996 import divide_5996

def test_add_5993():
    assert add_5993(2, 3) == 5

def test_subtract_5994():
    assert subtract_5994(10, 4) == 6

def test_multiply_5995():
    assert multiply_5995(3, 7) == 21

def test_divide_5996():
    assert divide_5996(10, 2) == 5.0
