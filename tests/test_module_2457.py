"""Tests for test module 2457 — covers src modules [9825, 9826, 9827, 9828]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9825 import add_9825
from module_9826 import subtract_9826
from module_9827 import multiply_9827
from module_9828 import divide_9828

def test_add_9825():
    assert add_9825(2, 3) == 5

def test_subtract_9826():
    assert subtract_9826(10, 4) == 6

def test_multiply_9827():
    assert multiply_9827(3, 7) == 21

def test_divide_9828():
    assert divide_9828(10, 2) == 5.0
