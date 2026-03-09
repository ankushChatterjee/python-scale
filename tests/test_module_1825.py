"""Tests for test module 1825 — covers src modules [7297, 7298, 7299, 7300]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7297 import add_7297
from module_7298 import subtract_7298
from module_7299 import multiply_7299
from module_7300 import divide_7300

def test_add_7297():
    assert add_7297(2, 3) == 5

def test_subtract_7298():
    assert subtract_7298(10, 4) == 6

def test_multiply_7299():
    assert multiply_7299(3, 7) == 21

def test_divide_7300():
    assert divide_7300(10, 2) == 5.0
