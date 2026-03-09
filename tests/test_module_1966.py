"""Tests for test module 1966 — covers src modules [7861, 7862, 7863, 7864]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7861 import modulo_7861
from module_7862 import power_7862
from module_7863 import min_7863
from module_7864 import max_7864

def test_modulo_7861():
    assert modulo_7861(10, 3) == 1

def test_power_7862():
    assert power_7862(2, 8) == 256

def test_min_7863():
    assert min_7863(3, 7) == 3

def test_max_7864():
    assert max_7864(3, 7) == 7
