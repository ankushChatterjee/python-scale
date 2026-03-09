"""Tests for test module 89 — covers src modules [353, 354, 355, 356]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_353 import add_353
from module_354 import subtract_354
from module_355 import multiply_355
from module_356 import divide_356

def test_add_353():
    assert add_353(2, 3) == 5

def test_subtract_354():
    assert subtract_354(10, 4) == 6

def test_multiply_355():
    assert multiply_355(3, 7) == 21

def test_divide_356():
    assert divide_356(10, 2) == 5.0
