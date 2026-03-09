"""Tests for test module 1838 — covers src modules [7349, 7350, 7351, 7352]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7349 import modulo_7349
from module_7350 import power_7350
from module_7351 import min_7351
from module_7352 import max_7352

def test_modulo_7349():
    assert modulo_7349(10, 3) == 1

def test_power_7350():
    assert power_7350(2, 8) == 256

def test_min_7351():
    assert min_7351(3, 7) == 3

def test_max_7352():
    assert max_7352(3, 7) == 7
