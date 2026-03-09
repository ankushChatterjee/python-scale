"""Tests for test module 599 — covers src modules [2393, 2394, 2395, 2396]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2393 import add_2393
from module_2394 import subtract_2394
from module_2395 import multiply_2395
from module_2396 import divide_2396

def test_add_2393():
    assert add_2393(2, 3) == 5

def test_subtract_2394():
    assert subtract_2394(10, 4) == 6

def test_multiply_2395():
    assert multiply_2395(3, 7) == 21

def test_divide_2396():
    assert divide_2396(10, 2) == 5.0
