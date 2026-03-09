"""Tests for test module 2305 — covers src modules [9217, 9218, 9219, 9220]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9217 import add_9217
from module_9218 import subtract_9218
from module_9219 import multiply_9219
from module_9220 import divide_9220

def test_add_9217():
    assert add_9217(2, 3) == 5

def test_subtract_9218():
    assert subtract_9218(10, 4) == 6

def test_multiply_9219():
    assert multiply_9219(3, 7) == 21

def test_divide_9220():
    assert divide_9220(10, 2) == 5.0
