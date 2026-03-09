"""Tests for test module 1219 — covers src modules [4873, 4874, 4875, 4876]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4873 import add_4873
from module_4874 import subtract_4874
from module_4875 import multiply_4875
from module_4876 import divide_4876

def test_add_4873():
    assert add_4873(2, 3) == 5

def test_subtract_4874():
    assert subtract_4874(10, 4) == 6

def test_multiply_4875():
    assert multiply_4875(3, 7) == 21

def test_divide_4876():
    assert divide_4876(10, 2) == 5.0
