"""Tests for test module 838 — covers src modules [3349, 3350, 3351, 3352]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3349 import modulo_3349
from module_3350 import power_3350
from module_3351 import min_3351
from module_3352 import max_3352

def test_modulo_3349():
    assert modulo_3349(10, 3) == 1

def test_power_3350():
    assert power_3350(2, 8) == 256

def test_min_3351():
    assert min_3351(3, 7) == 3

def test_max_3352():
    assert max_3352(3, 7) == 7
