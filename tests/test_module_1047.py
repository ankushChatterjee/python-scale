"""Tests for test module 1047 — covers src modules [4185, 4186, 4187, 4188]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4185 import add_4185
from module_4186 import subtract_4186
from module_4187 import multiply_4187
from module_4188 import divide_4188

def test_add_4185():
    assert add_4185(2, 3) == 5

def test_subtract_4186():
    assert subtract_4186(10, 4) == 6

def test_multiply_4187():
    assert multiply_4187(3, 7) == 21

def test_divide_4188():
    assert divide_4188(10, 2) == 5.0
