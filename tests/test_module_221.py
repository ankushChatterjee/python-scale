"""Tests for test module 221 — covers src modules [881, 882, 883, 884]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_881 import add_881
from module_882 import subtract_882
from module_883 import multiply_883
from module_884 import divide_884

def test_add_881():
    assert add_881(2, 3) == 5

def test_subtract_882():
    assert subtract_882(10, 4) == 6

def test_multiply_883():
    assert multiply_883(3, 7) == 21

def test_divide_884():
    assert divide_884(10, 2) == 5.0
