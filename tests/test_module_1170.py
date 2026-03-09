"""Tests for test module 1170 — covers src modules [4677, 4678, 4679, 4680]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4677 import modulo_4677
from module_4678 import power_4678
from module_4679 import min_4679
from module_4680 import max_4680

def test_modulo_4677():
    assert modulo_4677(10, 3) == 1

def test_power_4678():
    assert power_4678(2, 8) == 256

def test_min_4679():
    assert min_4679(3, 7) == 3

def test_max_4680():
    assert max_4680(3, 7) == 7
