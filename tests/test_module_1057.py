"""Tests for test module 1057 — covers src modules [4225, 4226, 4227, 4228]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4225 import add_4225
from module_4226 import subtract_4226
from module_4227 import multiply_4227
from module_4228 import divide_4228

def test_add_4225():
    assert add_4225(2, 3) == 5

def test_subtract_4226():
    assert subtract_4226(10, 4) == 6

def test_multiply_4227():
    assert multiply_4227(3, 7) == 21

def test_divide_4228():
    assert divide_4228(10, 2) == 5.0
