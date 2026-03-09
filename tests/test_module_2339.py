"""Tests for test module 2339 — covers src modules [9353, 9354, 9355, 9356]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9353 import add_9353
from module_9354 import subtract_9354
from module_9355 import multiply_9355
from module_9356 import divide_9356

def test_add_9353():
    assert add_9353(2, 3) == 5

def test_subtract_9354():
    assert subtract_9354(10, 4) == 6

def test_multiply_9355():
    assert multiply_9355(3, 7) == 21

def test_divide_9356():
    assert divide_9356(10, 2) == 5.0
