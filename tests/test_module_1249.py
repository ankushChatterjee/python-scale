"""Tests for test module 1249 — covers src modules [4993, 4994, 4995, 4996]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4993 import add_4993
from module_4994 import subtract_4994
from module_4995 import multiply_4995
from module_4996 import divide_4996

def test_add_4993():
    assert add_4993(2, 3) == 5

def test_subtract_4994():
    assert subtract_4994(10, 4) == 6

def test_multiply_4995():
    assert multiply_4995(3, 7) == 21

def test_divide_4996():
    assert divide_4996(10, 2) == 5.0
