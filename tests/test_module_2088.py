"""Tests for test module 2088 — covers src modules [8349, 8350, 8351, 8352]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8349 import modulo_8349
from module_8350 import power_8350
from module_8351 import min_8351
from module_8352 import max_8352

def test_modulo_8349():
    assert modulo_8349(10, 3) == 1

def test_power_8350():
    assert power_8350(2, 8) == 256

def test_min_8351():
    assert min_8351(3, 7) == 3

def test_max_8352():
    assert max_8352(3, 7) == 7
