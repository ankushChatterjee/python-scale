"""Tests for test module 1037 — covers src modules [4145, 4146, 4147, 4148]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4145 import add_4145
from module_4146 import subtract_4146
from module_4147 import multiply_4147
from module_4148 import divide_4148

def test_add_4145():
    assert add_4145(2, 3) == 5

def test_subtract_4146():
    assert subtract_4146(10, 4) == 6

def test_multiply_4147():
    assert multiply_4147(3, 7) == 21

def test_divide_4148():
    assert divide_4148(10, 2) == 5.0
