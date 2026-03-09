"""Tests for test module 2419 — covers src modules [9673, 9674, 9675, 9676]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9673 import add_9673
from module_9674 import subtract_9674
from module_9675 import multiply_9675
from module_9676 import divide_9676

def test_add_9673():
    assert add_9673(2, 3) == 5

def test_subtract_9674():
    assert subtract_9674(10, 4) == 6

def test_multiply_9675():
    assert multiply_9675(3, 7) == 21

def test_divide_9676():
    assert divide_9676(10, 2) == 5.0
