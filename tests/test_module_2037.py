"""Tests for test module 2037 — covers src modules [8145, 8146, 8147, 8148]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8145 import add_8145
from module_8146 import subtract_8146
from module_8147 import multiply_8147
from module_8148 import divide_8148

def test_add_8145():
    assert add_8145(2, 3) == 5

def test_subtract_8146():
    assert subtract_8146(10, 4) == 6

def test_multiply_8147():
    assert multiply_8147(3, 7) == 21

def test_divide_8148():
    assert divide_8148(10, 2) == 5.0
