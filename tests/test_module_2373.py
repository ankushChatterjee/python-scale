"""Tests for test module 2373 — covers src modules [9489, 9490, 9491, 9492]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9489 import add_9489
from module_9490 import subtract_9490
from module_9491 import multiply_9491
from module_9492 import divide_9492

def test_add_9489():
    assert add_9489(2, 3) == 5

def test_subtract_9490():
    assert subtract_9490(10, 4) == 6

def test_multiply_9491():
    assert multiply_9491(3, 7) == 21

def test_divide_9492():
    assert divide_9492(10, 2) == 5.0
