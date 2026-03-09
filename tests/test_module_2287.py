"""Tests for test module 2287 — covers src modules [9145, 9146, 9147, 9148]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9145 import add_9145
from module_9146 import subtract_9146
from module_9147 import multiply_9147
from module_9148 import divide_9148

def test_add_9145():
    assert add_9145(2, 3) == 5

def test_subtract_9146():
    assert subtract_9146(10, 4) == 6

def test_multiply_9147():
    assert multiply_9147(3, 7) == 21

def test_divide_9148():
    assert divide_9148(10, 2) == 5.0
