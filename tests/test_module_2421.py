"""Tests for test module 2421 — covers src modules [9681, 9682, 9683, 9684]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9681 import add_9681
from module_9682 import subtract_9682
from module_9683 import multiply_9683
from module_9684 import divide_9684

def test_add_9681():
    assert add_9681(2, 3) == 5

def test_subtract_9682():
    assert subtract_9682(10, 4) == 6

def test_multiply_9683():
    assert multiply_9683(3, 7) == 21

def test_divide_9684():
    assert divide_9684(10, 2) == 5.0
