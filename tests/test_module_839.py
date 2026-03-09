"""Tests for test module 839 — covers src modules [3353, 3354, 3355, 3356]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3353 import add_3353
from module_3354 import subtract_3354
from module_3355 import multiply_3355
from module_3356 import divide_3356

def test_add_3353():
    assert add_3353(2, 3) == 5

def test_subtract_3354():
    assert subtract_3354(10, 4) == 6

def test_multiply_3355():
    assert multiply_3355(3, 7) == 21

def test_divide_3356():
    assert divide_3356(10, 2) == 5.0
