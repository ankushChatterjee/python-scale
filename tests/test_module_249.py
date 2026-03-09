"""Tests for test module 249 — covers src modules [993, 994, 995, 996]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_993 import add_993
from module_994 import subtract_994
from module_995 import multiply_995
from module_996 import divide_996

def test_add_993():
    assert add_993(2, 3) == 5

def test_subtract_994():
    assert subtract_994(10, 4) == 6

def test_multiply_995():
    assert multiply_995(3, 7) == 21

def test_divide_996():
    assert divide_996(10, 2) == 5.0
