"""Tests for test module 2407 — covers src modules [9625, 9626, 9627, 9628]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9625 import add_9625
from module_9626 import subtract_9626
from module_9627 import multiply_9627
from module_9628 import divide_9628

def test_add_9625():
    assert add_9625(2, 3) == 5

def test_subtract_9626():
    assert subtract_9626(10, 4) == 6

def test_multiply_9627():
    assert multiply_9627(3, 7) == 21

def test_divide_9628():
    assert divide_9628(10, 2) == 5.0
