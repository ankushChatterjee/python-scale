"""Tests for test module 1264 — covers src modules [5053, 5054, 5055, 5056]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5053 import modulo_5053
from module_5054 import power_5054
from module_5055 import min_5055
from module_5056 import max_5056

def test_modulo_5053():
    assert modulo_5053(10, 3) == 1

def test_power_5054():
    assert power_5054(2, 8) == 256

def test_min_5055():
    assert min_5055(3, 7) == 3

def test_max_5056():
    assert max_5056(3, 7) == 7
