"""Tests for test module 803 — covers src modules [3209, 3210, 3211, 3212]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3209 import add_3209
from module_3210 import subtract_3210
from module_3211 import multiply_3211
from module_3212 import divide_3212

def test_add_3209():
    assert add_3209(2, 3) == 5

def test_subtract_3210():
    assert subtract_3210(10, 4) == 6

def test_multiply_3211():
    assert multiply_3211(3, 7) == 21

def test_divide_3212():
    assert divide_3212(10, 2) == 5.0
