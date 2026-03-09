"""Tests for test module 1223 — covers src modules [4889, 4890, 4891, 4892]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4889 import add_4889
from module_4890 import subtract_4890
from module_4891 import multiply_4891
from module_4892 import divide_4892

def test_add_4889():
    assert add_4889(2, 3) == 5

def test_subtract_4890():
    assert subtract_4890(10, 4) == 6

def test_multiply_4891():
    assert multiply_4891(3, 7) == 21

def test_divide_4892():
    assert divide_4892(10, 2) == 5.0
