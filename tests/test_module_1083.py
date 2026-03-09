"""Tests for test module 1083 — covers src modules [4329, 4330, 4331, 4332]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4329 import add_4329
from module_4330 import subtract_4330
from module_4331 import multiply_4331
from module_4332 import divide_4332

def test_add_4329():
    assert add_4329(2, 3) == 5

def test_subtract_4330():
    assert subtract_4330(10, 4) == 6

def test_multiply_4331():
    assert multiply_4331(3, 7) == 21

def test_divide_4332():
    assert divide_4332(10, 2) == 5.0
