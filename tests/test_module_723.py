"""Tests for test module 723 — covers src modules [2889, 2890, 2891, 2892]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2889 import add_2889
from module_2890 import subtract_2890
from module_2891 import multiply_2891
from module_2892 import divide_2892

def test_add_2889():
    assert add_2889(2, 3) == 5

def test_subtract_2890():
    assert subtract_2890(10, 4) == 6

def test_multiply_2891():
    assert multiply_2891(3, 7) == 21

def test_divide_2892():
    assert divide_2892(10, 2) == 5.0
