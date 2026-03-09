"""Tests for test module 2499 — covers src modules [9993, 9994, 9995, 9996]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9993 import add_9993
from module_9994 import subtract_9994
from module_9995 import multiply_9995
from module_9996 import divide_9996

def test_add_9993():
    assert add_9993(2, 3) == 5

def test_subtract_9994():
    assert subtract_9994(10, 4) == 6

def test_multiply_9995():
    assert multiply_9995(3, 7) == 21

def test_divide_9996():
    assert divide_9996(10, 2) == 5.0
