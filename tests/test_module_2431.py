"""Tests for test module 2431 — covers src modules [9721, 9722, 9723, 9724]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9721 import add_9721
from module_9722 import subtract_9722
from module_9723 import multiply_9723
from module_9724 import divide_9724

def test_add_9721():
    assert add_9721(2, 3) == 5

def test_subtract_9722():
    assert subtract_9722(10, 4) == 6

def test_multiply_9723():
    assert multiply_9723(3, 7) == 21

def test_divide_9724():
    assert divide_9724(10, 2) == 5.0
