"""Tests for test module 91 — covers src modules [361, 362, 363, 364]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_361 import add_361
from module_362 import subtract_362
from module_363 import multiply_363
from module_364 import divide_364

def test_add_361():
    assert add_361(2, 3) == 5

def test_subtract_362():
    assert subtract_362(10, 4) == 6

def test_multiply_363():
    assert multiply_363(3, 7) == 21

def test_divide_364():
    assert divide_364(10, 2) == 5.0
