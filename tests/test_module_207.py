"""Tests for test module 207 — covers src modules [825, 826, 827, 828]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_825 import add_825
from module_826 import subtract_826
from module_827 import multiply_827
from module_828 import divide_828

def test_add_825():
    assert add_825(2, 3) == 5

def test_subtract_826():
    assert subtract_826(10, 4) == 6

def test_multiply_827():
    assert multiply_827(3, 7) == 21

def test_divide_828():
    assert divide_828(10, 2) == 5.0
