"""Tests for test module 797 — covers src modules [3185, 3186, 3187, 3188]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3185 import add_3185
from module_3186 import subtract_3186
from module_3187 import multiply_3187
from module_3188 import divide_3188

def test_add_3185():
    assert add_3185(2, 3) == 5

def test_subtract_3186():
    assert subtract_3186(10, 4) == 6

def test_multiply_3187():
    assert multiply_3187(3, 7) == 21

def test_divide_3188():
    assert divide_3188(10, 2) == 5.0
