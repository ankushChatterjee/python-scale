"""Tests for test module 307 — covers src modules [1225, 1226, 1227, 1228]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1225 import add_1225
from module_1226 import subtract_1226
from module_1227 import multiply_1227
from module_1228 import divide_1228

def test_add_1225():
    assert add_1225(2, 3) == 5

def test_subtract_1226():
    assert subtract_1226(10, 4) == 6

def test_multiply_1227():
    assert multiply_1227(3, 7) == 21

def test_divide_1228():
    assert divide_1228(10, 2) == 5.0
