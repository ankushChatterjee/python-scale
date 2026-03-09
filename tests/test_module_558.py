"""Tests for test module 558 — covers src modules [2229, 2230, 2231, 2232]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2229 import modulo_2229
from module_2230 import power_2230
from module_2231 import min_2231
from module_2232 import max_2232

def test_modulo_2229():
    assert modulo_2229(10, 3) == 1

def test_power_2230():
    assert power_2230(2, 8) == 256

def test_min_2231():
    assert min_2231(3, 7) == 3

def test_max_2232():
    assert max_2232(3, 7) == 7
