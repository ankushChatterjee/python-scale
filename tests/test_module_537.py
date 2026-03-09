"""Tests for test module 537 — covers src modules [2145, 2146, 2147, 2148]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2145 import add_2145
from module_2146 import subtract_2146
from module_2147 import multiply_2147
from module_2148 import divide_2148

def test_add_2145():
    assert add_2145(2, 3) == 5

def test_subtract_2146():
    assert subtract_2146(10, 4) == 6

def test_multiply_2147():
    assert multiply_2147(3, 7) == 21

def test_divide_2148():
    assert divide_2148(10, 2) == 5.0
