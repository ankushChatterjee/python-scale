"""Tests for test module 1338 — covers src modules [5349, 5350, 5351, 5352]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5349 import modulo_5349
from module_5350 import power_5350
from module_5351 import min_5351
from module_5352 import max_5352

def test_modulo_5349():
    assert modulo_5349(10, 3) == 1

def test_power_5350():
    assert power_5350(2, 8) == 256

def test_min_5351():
    assert min_5351(3, 7) == 3

def test_max_5352():
    assert max_5352(3, 7) == 7
