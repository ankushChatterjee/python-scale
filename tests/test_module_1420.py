"""Tests for test module 1420 — covers src modules [5677, 5678, 5679, 5680]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5677 import modulo_5677
from module_5678 import power_5678
from module_5679 import min_5679
from module_5680 import max_5680

def test_modulo_5677():
    assert modulo_5677(10, 3) == 1

def test_power_5678():
    assert power_5678(2, 8) == 256

def test_min_5679():
    assert min_5679(3, 7) == 3

def test_max_5680():
    assert max_5680(3, 7) == 7
