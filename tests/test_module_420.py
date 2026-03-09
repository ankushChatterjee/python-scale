"""Tests for test module 420 — covers src modules [1677, 1678, 1679, 1680]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1677 import modulo_1677
from module_1678 import power_1678
from module_1679 import min_1679
from module_1680 import max_1680

def test_modulo_1677():
    assert modulo_1677(10, 3) == 1

def test_power_1678():
    assert power_1678(2, 8) == 256

def test_min_1679():
    assert min_1679(3, 7) == 3

def test_max_1680():
    assert max_1680(3, 7) == 7
