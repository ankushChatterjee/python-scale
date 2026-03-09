"""Tests for test module 291 — covers src modules [1161, 1162, 1163, 1164]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1161 import add_1161
from module_1162 import subtract_1162
from module_1163 import multiply_1163
from module_1164 import divide_1164

def test_add_1161():
    assert add_1161(2, 3) == 5

def test_subtract_1162():
    assert subtract_1162(10, 4) == 6

def test_multiply_1163():
    assert multiply_1163(3, 7) == 21

def test_divide_1164():
    assert divide_1164(10, 2) == 5.0
