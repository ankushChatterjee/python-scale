"""Tests for test module 2371 — covers src modules [9481, 9482, 9483, 9484]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9481 import add_9481
from module_9482 import subtract_9482
from module_9483 import multiply_9483
from module_9484 import divide_9484

def test_add_9481():
    assert add_9481(2, 3) == 5

def test_subtract_9482():
    assert subtract_9482(10, 4) == 6

def test_multiply_9483():
    assert multiply_9483(3, 7) == 21

def test_divide_9484():
    assert divide_9484(10, 2) == 5.0
