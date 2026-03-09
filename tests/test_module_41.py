"""Tests for test module 41 — covers src modules [161, 162, 163, 164]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_161 import add_161
from module_162 import subtract_162
from module_163 import multiply_163
from module_164 import divide_164

def test_add_161():
    assert add_161(2, 3) == 5

def test_subtract_162():
    assert subtract_162(10, 4) == 6

def test_multiply_163():
    assert multiply_163(3, 7) == 21

def test_divide_164():
    assert divide_164(10, 2) == 5.0
