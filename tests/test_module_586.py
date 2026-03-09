"""Tests for test module 586 — covers src modules [2341, 2342, 2343, 2344]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2341 import modulo_2341
from module_2342 import power_2342
from module_2343 import min_2343
from module_2344 import max_2344

def test_modulo_2341():
    assert modulo_2341(10, 3) == 1

def test_power_2342():
    assert power_2342(2, 8) == 256

def test_min_2343():
    assert min_2343(3, 7) == 3

def test_max_2344():
    assert max_2344(3, 7) == 7
