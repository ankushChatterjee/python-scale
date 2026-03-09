"""Tests for test module 836 — covers src modules [3341, 3342, 3343, 3344]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3341 import modulo_3341
from module_3342 import power_3342
from module_3343 import min_3343
from module_3344 import max_3344

def test_modulo_3341():
    assert modulo_3341(10, 3) == 1

def test_power_3342():
    assert power_3342(2, 8) == 256

def test_min_3343():
    assert min_3343(3, 7) == 3

def test_max_3344():
    assert max_3344(3, 7) == 7
