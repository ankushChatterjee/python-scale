"""Tests for test module 1764 — covers src modules [7053, 7054, 7055, 7056]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7053 import modulo_7053
from module_7054 import power_7054
from module_7055 import min_7055
from module_7056 import max_7056

def test_modulo_7053():
    assert modulo_7053(10, 3) == 1

def test_power_7054():
    assert power_7054(2, 8) == 256

def test_min_7055():
    assert min_7055(3, 7) == 3

def test_max_7056():
    assert max_7056(3, 7) == 7
