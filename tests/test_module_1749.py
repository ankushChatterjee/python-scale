"""Tests for test module 1749 — covers src modules [6993, 6994, 6995, 6996]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6993 import add_6993
from module_6994 import subtract_6994
from module_6995 import multiply_6995
from module_6996 import divide_6996

def test_add_6993():
    assert add_6993(2, 3) == 5

def test_subtract_6994():
    assert subtract_6994(10, 4) == 6

def test_multiply_6995():
    assert multiply_6995(3, 7) == 21

def test_divide_6996():
    assert divide_6996(10, 2) == 5.0
