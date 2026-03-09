"""Tests for test module 57 — covers src modules [225, 226, 227, 228]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_225 import add_225
from module_226 import subtract_226
from module_227 import multiply_227
from module_228 import divide_228

def test_add_225():
    assert add_225(2, 3) == 5

def test_subtract_226():
    assert subtract_226(10, 4) == 6

def test_multiply_227():
    assert multiply_227(3, 7) == 21

def test_divide_228():
    assert divide_228(10, 2) == 5.0
