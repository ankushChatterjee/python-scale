"""Tests for test module 592 — covers src modules [2365, 2366, 2367, 2368]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2365 import modulo_2365
from module_2366 import power_2366
from module_2367 import min_2367
from module_2368 import max_2368

def test_modulo_2365():
    assert modulo_2365(10, 3) == 1

def test_power_2366():
    assert power_2366(2, 8) == 256

def test_min_2367():
    assert min_2367(3, 7) == 3

def test_max_2368():
    assert max_2368(3, 7) == 7
