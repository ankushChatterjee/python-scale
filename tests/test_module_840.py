"""Tests for test module 840 — covers src modules [3357, 3358, 3359, 3360]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3357 import modulo_3357
from module_3358 import power_3358
from module_3359 import min_3359
from module_3360 import max_3360

def test_modulo_3357():
    assert modulo_3357(10, 3) == 1

def test_power_3358():
    assert power_3358(2, 8) == 256

def test_min_3359():
    assert min_3359(3, 7) == 3

def test_max_3360():
    assert max_3360(3, 7) == 7
