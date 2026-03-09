"""Tests for test module 2201 — covers src modules [8801, 8802, 8803, 8804]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8801 import add_8801
from module_8802 import subtract_8802
from module_8803 import multiply_8803
from module_8804 import divide_8804

def test_add_8801():
    assert add_8801(2, 3) == 5

def test_subtract_8802():
    assert subtract_8802(10, 4) == 6

def test_multiply_8803():
    assert multiply_8803(3, 7) == 21

def test_divide_8804():
    assert divide_8804(10, 2) == 5.0
