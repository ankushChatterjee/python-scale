"""Tests for test module 297 — covers src modules [1185, 1186, 1187, 1188]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1185 import add_1185
from module_1186 import subtract_1186
from module_1187 import multiply_1187
from module_1188 import divide_1188

def test_add_1185():
    assert add_1185(2, 3) == 5

def test_subtract_1186():
    assert subtract_1186(10, 4) == 6

def test_multiply_1187():
    assert multiply_1187(3, 7) == 21

def test_divide_1188():
    assert divide_1188(10, 2) == 5.0
