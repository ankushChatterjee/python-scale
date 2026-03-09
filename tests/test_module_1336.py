"""Tests for test module 1336 — covers src modules [5341, 5342, 5343, 5344]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5341 import modulo_5341
from module_5342 import power_5342
from module_5343 import min_5343
from module_5344 import max_5344

def test_modulo_5341():
    assert modulo_5341(10, 3) == 1

def test_power_5342():
    assert power_5342(2, 8) == 256

def test_min_5343():
    assert min_5343(3, 7) == 3

def test_max_5344():
    assert max_5344(3, 7) == 7
