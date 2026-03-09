"""Tests for test module 2323 — covers src modules [9289, 9290, 9291, 9292]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9289 import add_9289
from module_9290 import subtract_9290
from module_9291 import multiply_9291
from module_9292 import divide_9292

def test_add_9289():
    assert add_9289(2, 3) == 5

def test_subtract_9290():
    assert subtract_9290(10, 4) == 6

def test_multiply_9291():
    assert multiply_9291(3, 7) == 21

def test_divide_9292():
    assert divide_9292(10, 2) == 5.0
