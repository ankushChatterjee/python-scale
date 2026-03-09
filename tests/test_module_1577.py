"""Tests for test module 1577 — covers src modules [6305, 6306, 6307, 6308]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6305 import add_6305
from module_6306 import subtract_6306
from module_6307 import multiply_6307
from module_6308 import divide_6308

def test_add_6305():
    assert add_6305(2, 3) == 5

def test_subtract_6306():
    assert subtract_6306(10, 4) == 6

def test_multiply_6307():
    assert multiply_6307(3, 7) == 21

def test_divide_6308():
    assert divide_6308(10, 2) == 5.0
