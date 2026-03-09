"""Tests for test module 55 — covers src modules [217, 218, 219, 220]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_217 import add_217
from module_218 import subtract_218
from module_219 import multiply_219
from module_220 import divide_220

def test_add_217():
    assert add_217(2, 3) == 5

def test_subtract_218():
    assert subtract_218(10, 4) == 6

def test_multiply_219():
    assert multiply_219(3, 7) == 21

def test_divide_220():
    assert divide_220(10, 2) == 5.0
