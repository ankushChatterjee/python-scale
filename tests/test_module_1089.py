"""Tests for test module 1089 — covers src modules [4353, 4354, 4355, 4356]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4353 import add_4353
from module_4354 import subtract_4354
from module_4355 import multiply_4355
from module_4356 import divide_4356

def test_add_4353():
    assert add_4353(2, 3) == 5

def test_subtract_4354():
    assert subtract_4354(10, 4) == 6

def test_multiply_4355():
    assert multiply_4355(3, 7) == 21

def test_divide_4356():
    assert divide_4356(10, 2) == 5.0
