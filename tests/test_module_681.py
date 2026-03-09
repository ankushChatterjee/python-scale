"""Tests for test module 681 — covers src modules [2721, 2722, 2723, 2724]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2721 import add_2721
from module_2722 import subtract_2722
from module_2723 import multiply_2723
from module_2724 import divide_2724

def test_add_2721():
    assert add_2721(2, 3) == 5

def test_subtract_2722():
    assert subtract_2722(10, 4) == 6

def test_multiply_2723():
    assert multiply_2723(3, 7) == 21

def test_divide_2724():
    assert divide_2724(10, 2) == 5.0
