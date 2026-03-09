"""Tests for test module 669 — covers src modules [2673, 2674, 2675, 2676]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2673 import add_2673
from module_2674 import subtract_2674
from module_2675 import multiply_2675
from module_2676 import divide_2676

def test_add_2673():
    assert add_2673(2, 3) == 5

def test_subtract_2674():
    assert subtract_2674(10, 4) == 6

def test_multiply_2675():
    assert multiply_2675(3, 7) == 21

def test_divide_2676():
    assert divide_2676(10, 2) == 5.0
