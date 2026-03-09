"""Tests for test module 1670 — covers src modules [6677, 6678, 6679, 6680]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6677 import modulo_6677
from module_6678 import power_6678
from module_6679 import min_6679
from module_6680 import max_6680

def test_modulo_6677():
    assert modulo_6677(10, 3) == 1

def test_power_6678():
    assert power_6678(2, 8) == 256

def test_min_6679():
    assert min_6679(3, 7) == 3

def test_max_6680():
    assert max_6680(3, 7) == 7
