"""Tests for test module 95 — covers src modules [377, 378, 379, 380]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_377 import add_377
from module_378 import subtract_378
from module_379 import multiply_379
from module_380 import divide_380

def test_add_377():
    assert add_377(2, 3) == 5

def test_subtract_378():
    assert subtract_378(10, 4) == 6

def test_multiply_379():
    assert multiply_379(3, 7) == 21

def test_divide_380():
    assert divide_380(10, 2) == 5.0
