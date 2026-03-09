"""Tests for test module 2330 — covers src modules [9317, 9318, 9319, 9320]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9317 import modulo_9317
from module_9318 import power_9318
from module_9319 import min_9319
from module_9320 import max_9320

def test_modulo_9317():
    assert modulo_9317(10, 3) == 1

def test_power_9318():
    assert power_9318(2, 8) == 256

def test_min_9319():
    assert min_9319(3, 7) == 3

def test_max_9320():
    assert max_9320(3, 7) == 7
