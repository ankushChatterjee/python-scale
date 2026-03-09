"""Tests for test module 603 — covers src modules [2409, 2410, 2411, 2412]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2409 import add_2409
from module_2410 import subtract_2410
from module_2411 import multiply_2411
from module_2412 import divide_2412

def test_add_2409():
    assert add_2409(2, 3) == 5

def test_subtract_2410():
    assert subtract_2410(10, 4) == 6

def test_multiply_2411():
    assert multiply_2411(3, 7) == 21

def test_divide_2412():
    assert divide_2412(10, 2) == 5.0
