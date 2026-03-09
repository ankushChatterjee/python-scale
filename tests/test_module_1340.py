"""Tests for test module 1340 — covers src modules [5357, 5358, 5359, 5360]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5357 import modulo_5357
from module_5358 import power_5358
from module_5359 import min_5359
from module_5360 import max_5360

def test_modulo_5357():
    assert modulo_5357(10, 3) == 1

def test_power_5358():
    assert power_5358(2, 8) == 256

def test_min_5359():
    assert min_5359(3, 7) == 3

def test_max_5360():
    assert max_5360(3, 7) == 7
