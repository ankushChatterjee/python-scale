"""Tests for test module 1245 — covers src modules [4977, 4978, 4979, 4980]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4977 import add_4977
from module_4978 import subtract_4978
from module_4979 import multiply_4979
from module_4980 import divide_4980

def test_add_4977():
    assert add_4977(2, 3) == 5

def test_subtract_4978():
    assert subtract_4978(10, 4) == 6

def test_multiply_4979():
    assert multiply_4979(3, 7) == 21

def test_divide_4980():
    assert divide_4980(10, 2) == 5.0
