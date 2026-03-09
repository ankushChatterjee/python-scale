"""Tests for test module 338 — covers src modules [1349, 1350, 1351, 1352]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1349 import modulo_1349
from module_1350 import power_1350
from module_1351 import min_1351
from module_1352 import max_1352

def test_modulo_1349():
    assert modulo_1349(10, 3) == 1

def test_power_1350():
    assert power_1350(2, 8) == 256

def test_min_1351():
    assert min_1351(3, 7) == 3

def test_max_1352():
    assert max_1352(3, 7) == 7
