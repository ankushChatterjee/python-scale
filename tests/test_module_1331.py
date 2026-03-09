"""Tests for test module 1331 — covers src modules [5321, 5322, 5323, 5324]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5321 import add_5321
from module_5322 import subtract_5322
from module_5323 import multiply_5323
from module_5324 import divide_5324

def test_add_5321():
    assert add_5321(2, 3) == 5

def test_subtract_5322():
    assert subtract_5322(10, 4) == 6

def test_multiply_5323():
    assert multiply_5323(3, 7) == 21

def test_divide_5324():
    assert divide_5324(10, 2) == 5.0
