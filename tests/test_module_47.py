"""Tests for test module 47 — covers src modules [185, 186, 187, 188]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_185 import add_185
from module_186 import subtract_186
from module_187 import multiply_187
from module_188 import divide_188

def test_add_185():
    assert add_185(2, 3) == 5

def test_subtract_186():
    assert subtract_186(10, 4) == 6

def test_multiply_187():
    assert multiply_187(3, 7) == 21

def test_divide_188():
    assert divide_188(10, 2) == 5.0
