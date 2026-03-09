"""Tests for test module 308 — covers src modules [1229, 1230, 1231, 1232]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1229 import modulo_1229
from module_1230 import power_1230
from module_1231 import min_1231
from module_1232 import max_1232

def test_modulo_1229():
    assert modulo_1229(10, 3) == 1

def test_power_1230():
    assert power_1230(2, 8) == 256

def test_min_1231():
    assert min_1231(3, 7) == 3

def test_max_1232():
    assert max_1232(3, 7) == 7
