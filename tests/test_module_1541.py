"""Tests for test module 1541 — covers src modules [6161, 6162, 6163, 6164]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6161 import add_6161
from module_6162 import subtract_6162
from module_6163 import multiply_6163
from module_6164 import divide_6164

def test_add_6161():
    assert add_6161(2, 3) == 5

def test_subtract_6162():
    assert subtract_6162(10, 4) == 6

def test_multiply_6163():
    assert multiply_6163(3, 7) == 21

def test_divide_6164():
    assert divide_6164(10, 2) == 5.0
