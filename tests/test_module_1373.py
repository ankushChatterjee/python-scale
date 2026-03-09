"""Tests for test module 1373 — covers src modules [5489, 5490, 5491, 5492]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5489 import add_5489
from module_5490 import subtract_5490
from module_5491 import multiply_5491
from module_5492 import divide_5492

def test_add_5489():
    assert add_5489(2, 3) == 5

def test_subtract_5490():
    assert subtract_5490(10, 4) == 6

def test_multiply_5491():
    assert multiply_5491(3, 7) == 21

def test_divide_5492():
    assert divide_5492(10, 2) == 5.0
