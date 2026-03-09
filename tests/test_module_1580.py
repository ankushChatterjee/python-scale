"""Tests for test module 1580 — covers src modules [6317, 6318, 6319, 6320]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6317 import modulo_6317
from module_6318 import power_6318
from module_6319 import min_6319
from module_6320 import max_6320

def test_modulo_6317():
    assert modulo_6317(10, 3) == 1

def test_power_6318():
    assert power_6318(2, 8) == 256

def test_min_6319():
    assert min_6319(3, 7) == 3

def test_max_6320():
    assert max_6320(3, 7) == 7
