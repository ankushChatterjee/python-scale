"""Tests for test module 1920 — covers src modules [7677, 7678, 7679, 7680]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7677 import modulo_7677
from module_7678 import power_7678
from module_7679 import min_7679
from module_7680 import max_7680

def test_modulo_7677():
    assert modulo_7677(10, 3) == 1

def test_power_7678():
    assert power_7678(2, 8) == 256

def test_min_7679():
    assert min_7679(3, 7) == 3

def test_max_7680():
    assert max_7680(3, 7) == 7
