"""Tests for test module 2170 — covers src modules [8677, 8678, 8679, 8680]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8677 import modulo_8677
from module_8678 import power_8678
from module_8679 import min_8679
from module_8680 import max_8680

def test_modulo_8677():
    assert modulo_8677(10, 3) == 1

def test_power_8678():
    assert power_8678(2, 8) == 256

def test_min_8679():
    assert min_8679(3, 7) == 3

def test_max_8680():
    assert max_8680(3, 7) == 7
