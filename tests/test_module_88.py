"""Tests for test module 88 — covers src modules [349, 350, 351, 352]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_349 import modulo_349
from module_350 import power_350
from module_351 import min_351
from module_352 import max_352

def test_modulo_349():
    assert modulo_349(10, 3) == 1

def test_power_350():
    assert power_350(2, 8) == 256

def test_min_351():
    assert min_351(3, 7) == 3

def test_max_352():
    assert max_352(3, 7) == 7
