"""Tests for test module 1791 — covers src modules [7161, 7162, 7163, 7164]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7161 import add_7161
from module_7162 import subtract_7162
from module_7163 import multiply_7163
from module_7164 import divide_7164

def test_add_7161():
    assert add_7161(2, 3) == 5

def test_subtract_7162():
    assert subtract_7162(10, 4) == 6

def test_multiply_7163():
    assert multiply_7163(3, 7) == 21

def test_divide_7164():
    assert divide_7164(10, 2) == 5.0
