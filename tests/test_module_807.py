"""Tests for test module 807 — covers src modules [3225, 3226, 3227, 3228]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3225 import add_3225
from module_3226 import subtract_3226
from module_3227 import multiply_3227
from module_3228 import divide_3228

def test_add_3225():
    assert add_3225(2, 3) == 5

def test_subtract_3226():
    assert subtract_3226(10, 4) == 6

def test_multiply_3227():
    assert multiply_3227(3, 7) == 21

def test_divide_3228():
    assert divide_3228(10, 2) == 5.0
