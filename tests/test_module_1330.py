"""Tests for test module 1330 — covers src modules [5317, 5318, 5319, 5320]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5317 import modulo_5317
from module_5318 import power_5318
from module_5319 import min_5319
from module_5320 import max_5320

def test_modulo_5317():
    assert modulo_5317(10, 3) == 1

def test_power_5318():
    assert power_5318(2, 8) == 256

def test_min_5319():
    assert min_5319(3, 7) == 3

def test_max_5320():
    assert max_5320(3, 7) == 7
