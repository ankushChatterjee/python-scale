"""Tests for test module 670 — covers src modules [2677, 2678, 2679, 2680]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2677 import modulo_2677
from module_2678 import power_2678
from module_2679 import min_2679
from module_2680 import max_2680

def test_modulo_2677():
    assert modulo_2677(10, 3) == 1

def test_power_2678():
    assert power_2678(2, 8) == 256

def test_min_2679():
    assert min_2679(3, 7) == 3

def test_max_2680():
    assert max_2680(3, 7) == 7
