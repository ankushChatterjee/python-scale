"""Tests for test module 1839 — covers src modules [7353, 7354, 7355, 7356]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7353 import add_7353
from module_7354 import subtract_7354
from module_7355 import multiply_7355
from module_7356 import divide_7356

def test_add_7353():
    assert add_7353(2, 3) == 5

def test_subtract_7354():
    assert subtract_7354(10, 4) == 6

def test_multiply_7355():
    assert multiply_7355(3, 7) == 21

def test_divide_7356():
    assert divide_7356(10, 2) == 5.0
