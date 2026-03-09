"""Tests for test module 808 — covers src modules [3229, 3230, 3231, 3232]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3229 import modulo_3229
from module_3230 import power_3230
from module_3231 import min_3231
from module_3232 import max_3232

def test_modulo_3229():
    assert modulo_3229(10, 3) == 1

def test_power_3230():
    assert power_3230(2, 8) == 256

def test_min_3231():
    assert min_3231(3, 7) == 3

def test_max_3232():
    assert max_3232(3, 7) == 7
