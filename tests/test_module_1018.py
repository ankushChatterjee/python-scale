"""Tests for test module 1018 — covers src modules [4069, 4070, 4071, 4072]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4069 import modulo_4069
from module_4070 import power_4070
from module_4071 import min_4071
from module_4072 import max_4072

def test_modulo_4069():
    assert modulo_4069(10, 3) == 1

def test_power_4070():
    assert power_4070(2, 8) == 256

def test_min_4071():
    assert min_4071(3, 7) == 3

def test_max_4072():
    assert max_4072(3, 7) == 7
