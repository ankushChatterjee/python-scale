"""Tests for test module 1339 — covers src modules [5353, 5354, 5355, 5356]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5353 import add_5353
from module_5354 import subtract_5354
from module_5355 import multiply_5355
from module_5356 import divide_5356

def test_add_5353():
    assert add_5353(2, 3) == 5

def test_subtract_5354():
    assert subtract_5354(10, 4) == 6

def test_multiply_5355():
    assert multiply_5355(3, 7) == 21

def test_divide_5356():
    assert divide_5356(10, 2) == 5.0
