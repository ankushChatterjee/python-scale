"""Tests for test module 299 — covers src modules [1193, 1194, 1195, 1196]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1193 import add_1193
from module_1194 import subtract_1194
from module_1195 import multiply_1195
from module_1196 import divide_1196

def test_add_1193():
    assert add_1193(2, 3) == 5

def test_subtract_1194():
    assert subtract_1194(10, 4) == 6

def test_multiply_1195():
    assert multiply_1195(3, 7) == 21

def test_divide_1196():
    assert divide_1196(10, 2) == 5.0
