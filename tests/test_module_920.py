"""Tests for test module 920 — covers src modules [3677, 3678, 3679, 3680]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3677 import modulo_3677
from module_3678 import power_3678
from module_3679 import min_3679
from module_3680 import max_3680

def test_modulo_3677():
    assert modulo_3677(10, 3) == 1

def test_power_3678():
    assert power_3678(2, 8) == 256

def test_min_3679():
    assert min_3679(3, 7) == 3

def test_max_3680():
    assert max_3680(3, 7) == 7
