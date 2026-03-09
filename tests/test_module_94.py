"""Tests for test module 94 — covers src modules [373, 374, 375, 376]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_373 import modulo_373
from module_374 import power_374
from module_375 import min_375
from module_376 import max_376

def test_modulo_373():
    assert modulo_373(10, 3) == 1

def test_power_374():
    assert power_374(2, 8) == 256

def test_min_375():
    assert min_375(3, 7) == 3

def test_max_376():
    assert max_376(3, 7) == 7
