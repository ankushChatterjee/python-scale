"""Tests for test module 219 — covers src modules [873, 874, 875, 876]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_873 import add_873
from module_874 import subtract_874
from module_875 import multiply_875
from module_876 import divide_876

def test_add_873():
    assert add_873(2, 3) == 5

def test_subtract_874():
    assert subtract_874(10, 4) == 6

def test_multiply_875():
    assert multiply_875(3, 7) == 21

def test_divide_876():
    assert divide_876(10, 2) == 5.0
