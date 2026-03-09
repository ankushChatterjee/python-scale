"""Tests for test module 1547 — covers src modules [6185, 6186, 6187, 6188]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6185 import add_6185
from module_6186 import subtract_6186
from module_6187 import multiply_6187
from module_6188 import divide_6188

def test_add_6185():
    assert add_6185(2, 3) == 5

def test_subtract_6186():
    assert subtract_6186(10, 4) == 6

def test_multiply_6187():
    assert multiply_6187(3, 7) == 21

def test_divide_6188():
    assert divide_6188(10, 2) == 5.0
