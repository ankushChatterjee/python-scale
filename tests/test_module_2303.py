"""Tests for test module 2303 — covers src modules [9209, 9210, 9211, 9212]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9209 import add_9209
from module_9210 import subtract_9210
from module_9211 import multiply_9211
from module_9212 import divide_9212

def test_add_9209():
    assert add_9209(2, 3) == 5

def test_subtract_9210():
    assert subtract_9210(10, 4) == 6

def test_multiply_9211():
    assert multiply_9211(3, 7) == 21

def test_divide_9212():
    assert divide_9212(10, 2) == 5.0
