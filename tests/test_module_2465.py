"""Tests for test module 2465 — covers src modules [9857, 9858, 9859, 9860]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9857 import add_9857
from module_9858 import subtract_9858
from module_9859 import multiply_9859
from module_9860 import divide_9860

def test_add_9857():
    assert add_9857(2, 3) == 5

def test_subtract_9858():
    assert subtract_9858(10, 4) == 6

def test_multiply_9859():
    assert multiply_9859(3, 7) == 21

def test_divide_9860():
    assert divide_9860(10, 2) == 5.0
