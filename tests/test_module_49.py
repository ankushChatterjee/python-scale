"""Tests for test module 49 — covers src modules [193, 194, 195, 196]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_193 import add_193
from module_194 import subtract_194
from module_195 import multiply_195
from module_196 import divide_196

def test_add_193():
    assert add_193(2, 3) == 5

def test_subtract_194():
    assert subtract_194(10, 4) == 6

def test_multiply_195():
    assert multiply_195(3, 7) == 21

def test_divide_196():
    assert divide_196(10, 2) == 5.0
