"""Tests for test module 2249 — covers src modules [8993, 8994, 8995, 8996]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8993 import add_8993
from module_8994 import subtract_8994
from module_8995 import multiply_8995
from module_8996 import divide_8996

def test_add_8993():
    assert add_8993(2, 3) == 5

def test_subtract_8994():
    assert subtract_8994(10, 4) == 6

def test_multiply_8995():
    assert multiply_8995(3, 7) == 21

def test_divide_8996():
    assert divide_8996(10, 2) == 5.0
