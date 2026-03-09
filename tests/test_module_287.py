"""Tests for test module 287 — covers src modules [1145, 1146, 1147, 1148]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1145 import add_1145
from module_1146 import subtract_1146
from module_1147 import multiply_1147
from module_1148 import divide_1148

def test_add_1145():
    assert add_1145(2, 3) == 5

def test_subtract_1146():
    assert subtract_1146(10, 4) == 6

def test_multiply_1147():
    assert multiply_1147(3, 7) == 21

def test_divide_1148():
    assert divide_1148(10, 2) == 5.0
