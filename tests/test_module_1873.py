"""Tests for test module 1873 — covers src modules [7489, 7490, 7491, 7492]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7489 import add_7489
from module_7490 import subtract_7490
from module_7491 import multiply_7491
from module_7492 import divide_7492

def test_add_7489():
    assert add_7489(2, 3) == 5

def test_subtract_7490():
    assert subtract_7490(10, 4) == 6

def test_multiply_7491():
    assert multiply_7491(3, 7) == 21

def test_divide_7492():
    assert divide_7492(10, 2) == 5.0
