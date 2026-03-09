"""Tests for test module 2293 — covers src modules [9169, 9170, 9171, 9172]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9169 import add_9169
from module_9170 import subtract_9170
from module_9171 import multiply_9171
from module_9172 import divide_9172

def test_add_9169():
    assert add_9169(2, 3) == 5

def test_subtract_9170():
    assert subtract_9170(10, 4) == 6

def test_multiply_9171():
    assert multiply_9171(3, 7) == 21

def test_divide_9172():
    assert divide_9172(10, 2) == 5.0
