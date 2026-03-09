"""Tests for test module 2317 — covers src modules [9265, 9266, 9267, 9268]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9265 import add_9265
from module_9266 import subtract_9266
from module_9267 import multiply_9267
from module_9268 import divide_9268

def test_add_9265():
    assert add_9265(2, 3) == 5

def test_subtract_9266():
    assert subtract_9266(10, 4) == 6

def test_multiply_9267():
    assert multiply_9267(3, 7) == 21

def test_divide_9268():
    assert divide_9268(10, 2) == 5.0
