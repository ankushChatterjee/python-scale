"""Tests for test module 1701 — covers src modules [6801, 6802, 6803, 6804]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6801 import add_6801
from module_6802 import subtract_6802
from module_6803 import multiply_6803
from module_6804 import divide_6804

def test_add_6801():
    assert add_6801(2, 3) == 5

def test_subtract_6802():
    assert subtract_6802(10, 4) == 6

def test_multiply_6803():
    assert multiply_6803(3, 7) == 21

def test_divide_6804():
    assert divide_6804(10, 2) == 5.0
