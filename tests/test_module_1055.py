"""Tests for test module 1055 — covers src modules [4217, 4218, 4219, 4220]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4217 import add_4217
from module_4218 import subtract_4218
from module_4219 import multiply_4219
from module_4220 import divide_4220

def test_add_4217():
    assert add_4217(2, 3) == 5

def test_subtract_4218():
    assert subtract_4218(10, 4) == 6

def test_multiply_4219():
    assert multiply_4219(3, 7) == 21

def test_divide_4220():
    assert divide_4220(10, 2) == 5.0
