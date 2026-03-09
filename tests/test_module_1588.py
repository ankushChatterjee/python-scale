"""Tests for test module 1588 — covers src modules [6349, 6350, 6351, 6352]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6349 import modulo_6349
from module_6350 import power_6350
from module_6351 import min_6351
from module_6352 import max_6352

def test_modulo_6349():
    assert modulo_6349(10, 3) == 1

def test_power_6350():
    assert power_6350(2, 8) == 256

def test_min_6351():
    assert min_6351(3, 7) == 3

def test_max_6352():
    assert max_6352(3, 7) == 7
