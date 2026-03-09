"""Tests for test module 463 — covers src modules [1849, 1850, 1851, 1852]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1849 import add_1849
from module_1850 import subtract_1850
from module_1851 import multiply_1851
from module_1852 import divide_1852

def test_add_1849():
    assert add_1849(2, 3) == 5

def test_subtract_1850():
    assert subtract_1850(10, 4) == 6

def test_multiply_1851():
    assert multiply_1851(3, 7) == 21

def test_divide_1852():
    assert divide_1852(10, 2) == 5.0
