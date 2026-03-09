"""Tests for test module 1783 — covers src modules [7129, 7130, 7131, 7132]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7129 import add_7129
from module_7130 import subtract_7130
from module_7131 import multiply_7131
from module_7132 import divide_7132

def test_add_7129():
    assert add_7129(2, 3) == 5

def test_subtract_7130():
    assert subtract_7130(10, 4) == 6

def test_multiply_7131():
    assert multiply_7131(3, 7) == 21

def test_divide_7132():
    assert divide_7132(10, 2) == 5.0
