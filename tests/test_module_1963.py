"""Tests for test module 1963 — covers src modules [7849, 7850, 7851, 7852]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7849 import add_7849
from module_7850 import subtract_7850
from module_7851 import multiply_7851
from module_7852 import divide_7852

def test_add_7849():
    assert add_7849(2, 3) == 5

def test_subtract_7850():
    assert subtract_7850(10, 4) == 6

def test_multiply_7851():
    assert multiply_7851(3, 7) == 21

def test_divide_7852():
    assert divide_7852(10, 2) == 5.0
