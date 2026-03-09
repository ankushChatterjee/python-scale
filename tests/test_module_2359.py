"""Tests for test module 2359 — covers src modules [9433, 9434, 9435, 9436]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9433 import add_9433
from module_9434 import subtract_9434
from module_9435 import multiply_9435
from module_9436 import divide_9436

def test_add_9433():
    assert add_9433(2, 3) == 5

def test_subtract_9434():
    assert subtract_9434(10, 4) == 6

def test_multiply_9435():
    assert multiply_9435(3, 7) == 21

def test_divide_9436():
    assert divide_9436(10, 2) == 5.0
