"""Tests for test module 2055 — covers src modules [8217, 8218, 8219, 8220]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8217 import add_8217
from module_8218 import subtract_8218
from module_8219 import multiply_8219
from module_8220 import divide_8220

def test_add_8217():
    assert add_8217(2, 3) == 5

def test_subtract_8218():
    assert subtract_8218(10, 4) == 6

def test_multiply_8219():
    assert multiply_8219(3, 7) == 21

def test_divide_8220():
    assert divide_8220(10, 2) == 5.0
