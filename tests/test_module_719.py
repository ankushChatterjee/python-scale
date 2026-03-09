"""Tests for test module 719 — covers src modules [2873, 2874, 2875, 2876]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2873 import add_2873
from module_2874 import subtract_2874
from module_2875 import multiply_2875
from module_2876 import divide_2876

def test_add_2873():
    assert add_2873(2, 3) == 5

def test_subtract_2874():
    assert subtract_2874(10, 4) == 6

def test_multiply_2875():
    assert multiply_2875(3, 7) == 21

def test_divide_2876():
    assert divide_2876(10, 2) == 5.0
