"""Tests for test module 2018 — covers src modules [8069, 8070, 8071, 8072]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8069 import modulo_8069
from module_8070 import power_8070
from module_8071 import min_8071
from module_8072 import max_8072

def test_modulo_8069():
    assert modulo_8069(10, 3) == 1

def test_power_8070():
    assert power_8070(2, 8) == 256

def test_min_8071():
    assert min_8071(3, 7) == 3

def test_max_8072():
    assert max_8072(3, 7) == 7
