"""Tests for test module 2449 — covers src modules [9793, 9794, 9795, 9796]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9793 import add_9793
from module_9794 import subtract_9794
from module_9795 import multiply_9795
from module_9796 import divide_9796

def test_add_9793():
    assert add_9793(2, 3) == 5

def test_subtract_9794():
    assert subtract_9794(10, 4) == 6

def test_multiply_9795():
    assert multiply_9795(3, 7) == 21

def test_divide_9796():
    assert divide_9796(10, 2) == 5.0
