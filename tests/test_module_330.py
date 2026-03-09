"""Tests for test module 330 — covers src modules [1317, 1318, 1319, 1320]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1317 import modulo_1317
from module_1318 import power_1318
from module_1319 import min_1319
from module_1320 import max_1320

def test_modulo_1317():
    assert modulo_1317(10, 3) == 1

def test_power_1318():
    assert power_1318(2, 8) == 256

def test_min_1319():
    assert min_1319(3, 7) == 3

def test_max_1320():
    assert max_1320(3, 7) == 7
