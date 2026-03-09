"""Tests for test module 2283 — covers src modules [9129, 9130, 9131, 9132]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9129 import add_9129
from module_9130 import subtract_9130
from module_9131 import multiply_9131
from module_9132 import divide_9132

def test_add_9129():
    assert add_9129(2, 3) == 5

def test_subtract_9130():
    assert subtract_9130(10, 4) == 6

def test_multiply_9131():
    assert multiply_9131(3, 7) == 21

def test_divide_9132():
    assert divide_9132(10, 2) == 5.0
