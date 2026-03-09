"""Tests for test module 1558 — covers src modules [6229, 6230, 6231, 6232]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6229 import modulo_6229
from module_6230 import power_6230
from module_6231 import min_6231
from module_6232 import max_6232

def test_modulo_6229():
    assert modulo_6229(10, 3) == 1

def test_power_6230():
    assert power_6230(2, 8) == 256

def test_min_6231():
    assert min_6231(3, 7) == 3

def test_max_6232():
    assert max_6232(3, 7) == 7
