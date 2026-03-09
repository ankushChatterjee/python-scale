"""Tests for test module 2089 — covers src modules [8353, 8354, 8355, 8356]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8353 import add_8353
from module_8354 import subtract_8354
from module_8355 import multiply_8355
from module_8356 import divide_8356

def test_add_8353():
    assert add_8353(2, 3) == 5

def test_subtract_8354():
    assert subtract_8354(10, 4) == 6

def test_multiply_8355():
    assert multiply_8355(3, 7) == 21

def test_divide_8356():
    assert divide_8356(10, 2) == 5.0
