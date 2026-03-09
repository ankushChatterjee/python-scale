"""Tests for test module 1307 — covers src modules [5225, 5226, 5227, 5228]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5225 import add_5225
from module_5226 import subtract_5226
from module_5227 import multiply_5227
from module_5228 import divide_5228

def test_add_5225():
    assert add_5225(2, 3) == 5

def test_subtract_5226():
    assert subtract_5226(10, 4) == 6

def test_multiply_5227():
    assert multiply_5227(3, 7) == 21

def test_divide_5228():
    assert divide_5228(10, 2) == 5.0
