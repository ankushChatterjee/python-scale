"""Tests for test module 2171 — covers src modules [8681, 8682, 8683, 8684]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8681 import add_8681
from module_8682 import subtract_8682
from module_8683 import multiply_8683
from module_8684 import divide_8684

def test_add_8681():
    assert add_8681(2, 3) == 5

def test_subtract_8682():
    assert subtract_8682(10, 4) == 6

def test_multiply_8683():
    assert multiply_8683(3, 7) == 21

def test_divide_8684():
    assert divide_8684(10, 2) == 5.0
