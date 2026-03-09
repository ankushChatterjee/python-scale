"""Tests for test module 1291 — covers src modules [5161, 5162, 5163, 5164]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5161 import add_5161
from module_5162 import subtract_5162
from module_5163 import multiply_5163
from module_5164 import divide_5164

def test_add_5161():
    assert add_5161(2, 3) == 5

def test_subtract_5162():
    assert subtract_5162(10, 4) == 6

def test_multiply_5163():
    assert multiply_5163(3, 7) == 21

def test_divide_5164():
    assert divide_5164(10, 2) == 5.0
