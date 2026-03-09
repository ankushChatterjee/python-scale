"""Tests for test module 2473 — covers src modules [9889, 9890, 9891, 9892]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9889 import add_9889
from module_9890 import subtract_9890
from module_9891 import multiply_9891
from module_9892 import divide_9892

def test_add_9889():
    assert add_9889(2, 3) == 5

def test_subtract_9890():
    assert subtract_9890(10, 4) == 6

def test_multiply_9891():
    assert multiply_9891(3, 7) == 21

def test_divide_9892():
    assert divide_9892(10, 2) == 5.0
