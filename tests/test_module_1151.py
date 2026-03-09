"""Tests for test module 1151 — covers src modules [4601, 4602, 4603, 4604]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4601 import add_4601
from module_4602 import subtract_4602
from module_4603 import multiply_4603
from module_4604 import divide_4604

def test_add_4601():
    assert add_4601(2, 3) == 5

def test_subtract_4602():
    assert subtract_4602(10, 4) == 6

def test_multiply_4603():
    assert multiply_4603(3, 7) == 21

def test_divide_4604():
    assert divide_4604(10, 2) == 5.0
