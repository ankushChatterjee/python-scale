"""Tests for test module 580 — covers src modules [2317, 2318, 2319, 2320]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2317 import modulo_2317
from module_2318 import power_2318
from module_2319 import min_2319
from module_2320 import max_2320

def test_modulo_2317():
    assert modulo_2317(10, 3) == 1

def test_power_2318():
    assert power_2318(2, 8) == 256

def test_min_2319():
    assert min_2319(3, 7) == 3

def test_max_2320():
    assert max_2320(3, 7) == 7
