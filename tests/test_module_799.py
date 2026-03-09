"""Tests for test module 799 — covers src modules [3193, 3194, 3195, 3196]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3193 import add_3193
from module_3194 import subtract_3194
from module_3195 import multiply_3195
from module_3196 import divide_3196

def test_add_3193():
    assert add_3193(2, 3) == 5

def test_subtract_3194():
    assert subtract_3194(10, 4) == 6

def test_multiply_3195():
    assert multiply_3195(3, 7) == 21

def test_divide_3196():
    assert divide_3196(10, 2) == 5.0
