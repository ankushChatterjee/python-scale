"""Tests for test module 2058 — covers src modules [8229, 8230, 8231, 8232]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8229 import modulo_8229
from module_8230 import power_8230
from module_8231 import min_8231
from module_8232 import max_8232

def test_modulo_8229():
    assert modulo_8229(10, 3) == 1

def test_power_8230():
    assert power_8230(2, 8) == 256

def test_min_8231():
    assert min_8231(3, 7) == 3

def test_max_8232():
    assert max_8232(3, 7) == 7
