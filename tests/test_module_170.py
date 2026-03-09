"""Tests for test module 170 — covers src modules [677, 678, 679, 680]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_677 import modulo_677
from module_678 import power_678
from module_679 import min_679
from module_680 import max_680

def test_modulo_677():
    assert modulo_677(10, 3) == 1

def test_power_678():
    assert power_678(2, 8) == 256

def test_min_679():
    assert min_679(3, 7) == 3

def test_max_680():
    assert max_680(3, 7) == 7
