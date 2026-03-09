"""Tests for test module 2335 — covers src modules [9337, 9338, 9339, 9340]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9337 import add_9337
from module_9338 import subtract_9338
from module_9339 import multiply_9339
from module_9340 import divide_9340

def test_add_9337():
    assert add_9337(2, 3) == 5

def test_subtract_9338():
    assert subtract_9338(10, 4) == 6

def test_multiply_9339():
    assert multiply_9339(3, 7) == 21

def test_divide_9340():
    assert divide_9340(10, 2) == 5.0
