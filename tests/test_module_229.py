"""Tests for test module 229 — covers src modules [913, 914, 915, 916]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_913 import add_913
from module_914 import subtract_914
from module_915 import multiply_915
from module_916 import divide_916

def test_add_913():
    assert add_913(2, 3) == 5

def test_subtract_914():
    assert subtract_914(10, 4) == 6

def test_multiply_915():
    assert multiply_915(3, 7) == 21

def test_divide_916():
    assert divide_916(10, 2) == 5.0
