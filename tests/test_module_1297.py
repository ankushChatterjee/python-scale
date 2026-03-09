"""Tests for test module 1297 — covers src modules [5185, 5186, 5187, 5188]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5185 import add_5185
from module_5186 import subtract_5186
from module_5187 import multiply_5187
from module_5188 import divide_5188

def test_add_5185():
    assert add_5185(2, 3) == 5

def test_subtract_5186():
    assert subtract_5186(10, 4) == 6

def test_multiply_5187():
    assert multiply_5187(3, 7) == 21

def test_divide_5188():
    assert divide_5188(10, 2) == 5.0
