"""Tests for test module 268 — covers src modules [1069, 1070, 1071, 1072]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1069 import modulo_1069
from module_1070 import power_1070
from module_1071 import min_1071
from module_1072 import max_1072

def test_modulo_1069():
    assert modulo_1069(10, 3) == 1

def test_power_1070():
    assert power_1070(2, 8) == 256

def test_min_1071():
    assert min_1071(3, 7) == 3

def test_max_1072():
    assert max_1072(3, 7) == 7
