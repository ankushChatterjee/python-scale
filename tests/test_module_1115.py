"""Tests for test module 1115 — covers src modules [4457, 4458, 4459, 4460]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4457 import add_4457
from module_4458 import subtract_4458
from module_4459 import multiply_4459
from module_4460 import divide_4460

def test_add_4457():
    assert add_4457(2, 3) == 5

def test_subtract_4458():
    assert subtract_4458(10, 4) == 6

def test_multiply_4459():
    assert multiply_4459(3, 7) == 21

def test_divide_4460():
    assert divide_4460(10, 2) == 5.0
