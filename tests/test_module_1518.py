"""Tests for test module 1518 — covers src modules [6069, 6070, 6071, 6072]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6069 import modulo_6069
from module_6070 import power_6070
from module_6071 import min_6071
from module_6072 import max_6072

def test_modulo_6069():
    assert modulo_6069(10, 3) == 1

def test_power_6070():
    assert power_6070(2, 8) == 256

def test_min_6071():
    assert min_6071(3, 7) == 3

def test_max_6072():
    assert max_6072(3, 7) == 7
