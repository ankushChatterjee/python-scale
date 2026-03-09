"""Tests for test module 2333 — covers src modules [9329, 9330, 9331, 9332]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9329 import add_9329
from module_9330 import subtract_9330
from module_9331 import multiply_9331
from module_9332 import divide_9332

def test_add_9329():
    assert add_9329(2, 3) == 5

def test_subtract_9330():
    assert subtract_9330(10, 4) == 6

def test_multiply_9331():
    assert multiply_9331(3, 7) == 21

def test_divide_9332():
    assert divide_9332(10, 2) == 5.0
