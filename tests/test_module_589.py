"""Tests for test module 589 — covers src modules [2353, 2354, 2355, 2356]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2353 import add_2353
from module_2354 import subtract_2354
from module_2355 import multiply_2355
from module_2356 import divide_2356

def test_add_2353():
    assert add_2353(2, 3) == 5

def test_subtract_2354():
    assert subtract_2354(10, 4) == 6

def test_multiply_2355():
    assert multiply_2355(3, 7) == 21

def test_divide_2356():
    assert divide_2356(10, 2) == 5.0
