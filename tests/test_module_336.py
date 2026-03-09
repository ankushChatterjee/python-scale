"""Tests for test module 336 — covers src modules [1341, 1342, 1343, 1344]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1341 import modulo_1341
from module_1342 import power_1342
from module_1343 import min_1343
from module_1344 import max_1344

def test_modulo_1341():
    assert modulo_1341(10, 3) == 1

def test_power_1342():
    assert power_1342(2, 8) == 256

def test_min_1343():
    assert min_1343(3, 7) == 3

def test_max_1344():
    assert max_1344(3, 7) == 7
