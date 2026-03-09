"""Tests for test module 1088 — covers src modules [4349, 4350, 4351, 4352]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4349 import modulo_4349
from module_4350 import power_4350
from module_4351 import min_4351
from module_4352 import max_4352

def test_modulo_4349():
    assert modulo_4349(10, 3) == 1

def test_power_4350():
    assert power_4350(2, 8) == 256

def test_min_4351():
    assert min_4351(3, 7) == 3

def test_max_4352():
    assert max_4352(3, 7) == 7
