"""Tests for test module 1355 — covers src modules [5417, 5418, 5419, 5420]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5417 import add_5417
from module_5418 import subtract_5418
from module_5419 import multiply_5419
from module_5420 import divide_5420

def test_add_5417():
    assert add_5417(2, 3) == 5

def test_subtract_5418():
    assert subtract_5418(10, 4) == 6

def test_multiply_5419():
    assert multiply_5419(3, 7) == 21

def test_divide_5420():
    assert divide_5420(10, 2) == 5.0
