"""Tests for test module 703 — covers src modules [2809, 2810, 2811, 2812]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2809 import add_2809
from module_2810 import subtract_2810
from module_2811 import multiply_2811
from module_2812 import divide_2812

def test_add_2809():
    assert add_2809(2, 3) == 5

def test_subtract_2810():
    assert subtract_2810(10, 4) == 6

def test_multiply_2811():
    assert multiply_2811(3, 7) == 21

def test_divide_2812():
    assert divide_2812(10, 2) == 5.0
