"""Tests for test module 1797 — covers src modules [7185, 7186, 7187, 7188]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7185 import add_7185
from module_7186 import subtract_7186
from module_7187 import multiply_7187
from module_7188 import divide_7188

def test_add_7185():
    assert add_7185(2, 3) == 5

def test_subtract_7186():
    assert subtract_7186(10, 4) == 6

def test_multiply_7187():
    assert multiply_7187(3, 7) == 21

def test_divide_7188():
    assert divide_7188(10, 2) == 5.0
