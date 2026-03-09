"""Tests for test module 749 — covers src modules [2993, 2994, 2995, 2996]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2993 import add_2993
from module_2994 import subtract_2994
from module_2995 import multiply_2995
from module_2996 import divide_2996

def test_add_2993():
    assert add_2993(2, 3) == 5

def test_subtract_2994():
    assert subtract_2994(10, 4) == 6

def test_multiply_2995():
    assert multiply_2995(3, 7) == 21

def test_divide_2996():
    assert divide_2996(10, 2) == 5.0
