"""Tests for test module 693 — covers src modules [2769, 2770, 2771, 2772]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2769 import add_2769
from module_2770 import subtract_2770
from module_2771 import multiply_2771
from module_2772 import divide_2772

def test_add_2769():
    assert add_2769(2, 3) == 5

def test_subtract_2770():
    assert subtract_2770(10, 4) == 6

def test_multiply_2771():
    assert multiply_2771(3, 7) == 21

def test_divide_2772():
    assert divide_2772(10, 2) == 5.0
