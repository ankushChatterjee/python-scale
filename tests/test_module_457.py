"""Tests for test module 457 — covers src modules [1825, 1826, 1827, 1828]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1825 import add_1825
from module_1826 import subtract_1826
from module_1827 import multiply_1827
from module_1828 import divide_1828

def test_add_1825():
    assert add_1825(2, 3) == 5

def test_subtract_1826():
    assert subtract_1826(10, 4) == 6

def test_multiply_1827():
    assert multiply_1827(3, 7) == 21

def test_divide_1828():
    assert divide_1828(10, 2) == 5.0
