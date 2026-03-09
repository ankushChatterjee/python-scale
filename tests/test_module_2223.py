"""Tests for test module 2223 — covers src modules [8889, 8890, 8891, 8892]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8889 import add_8889
from module_8890 import subtract_8890
from module_8891 import multiply_8891
from module_8892 import divide_8892

def test_add_8889():
    assert add_8889(2, 3) == 5

def test_subtract_8890():
    assert subtract_8890(10, 4) == 6

def test_multiply_8891():
    assert multiply_8891(3, 7) == 21

def test_divide_8892():
    assert divide_8892(10, 2) == 5.0
