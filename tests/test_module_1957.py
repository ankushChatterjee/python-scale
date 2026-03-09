"""Tests for test module 1957 — covers src modules [7825, 7826, 7827, 7828]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7825 import add_7825
from module_7826 import subtract_7826
from module_7827 import multiply_7827
from module_7828 import divide_7828

def test_add_7825():
    assert add_7825(2, 3) == 5

def test_subtract_7826():
    assert subtract_7826(10, 4) == 6

def test_multiply_7827():
    assert multiply_7827(3, 7) == 21

def test_divide_7828():
    assert divide_7828(10, 2) == 5.0
