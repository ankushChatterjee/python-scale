"""Tests for test module 2428 — covers src modules [9709, 9710, 9711, 9712]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9709 import modulo_9709
from module_9710 import power_9710
from module_9711 import min_9711
from module_9712 import max_9712

def test_modulo_9709():
    assert modulo_9709(10, 3) == 1

def test_power_9710():
    assert power_9710(2, 8) == 256

def test_min_9711():
    assert min_9711(3, 7) == 3

def test_max_9712():
    assert max_9712(3, 7) == 7
