"""Tests for test module 2047 — covers src modules [8185, 8186, 8187, 8188]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8185 import add_8185
from module_8186 import subtract_8186
from module_8187 import multiply_8187
from module_8188 import divide_8188

def test_add_8185():
    assert add_8185(2, 3) == 5

def test_subtract_8186():
    assert subtract_8186(10, 4) == 6

def test_multiply_8187():
    assert multiply_8187(3, 7) == 21

def test_divide_8188():
    assert divide_8188(10, 2) == 5.0
