"""Tests for test module 1308 — covers src modules [5229, 5230, 5231, 5232]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5229 import modulo_5229
from module_5230 import power_5230
from module_5231 import min_5231
from module_5232 import max_5232

def test_modulo_5229():
    assert modulo_5229(10, 3) == 1

def test_power_5230():
    assert power_5230(2, 8) == 256

def test_min_5231():
    assert min_5231(3, 7) == 3

def test_max_5232():
    assert max_5232(3, 7) == 7
