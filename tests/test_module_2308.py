"""Tests for test module 2308 — covers src modules [9229, 9230, 9231, 9232]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9229 import modulo_9229
from module_9230 import power_9230
from module_9231 import min_9231
from module_9232 import max_9232

def test_modulo_9229():
    assert modulo_9229(10, 3) == 1

def test_power_9230():
    assert power_9230(2, 8) == 256

def test_min_9231():
    assert min_9231(3, 7) == 3

def test_max_9232():
    assert max_9232(3, 7) == 7
