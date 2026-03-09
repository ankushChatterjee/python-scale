"""Tests for test module 1522 — covers src modules [6085, 6086, 6087, 6088]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6085 import modulo_6085
from module_6086 import power_6086
from module_6087 import min_6087
from module_6088 import max_6088

def test_modulo_6085():
    assert modulo_6085(10, 3) == 1

def test_power_6086():
    assert power_6086(2, 8) == 256

def test_min_6087():
    assert min_6087(3, 7) == 3

def test_max_6088():
    assert max_6088(3, 7) == 7
