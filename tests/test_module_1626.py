"""Tests for test module 1626 — covers src modules [6501, 6502, 6503, 6504]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6501 import modulo_6501
from module_6502 import power_6502
from module_6503 import min_6503
from module_6504 import max_6504

def test_modulo_6501():
    assert modulo_6501(10, 3) == 1

def test_power_6502():
    assert power_6502(2, 8) == 256

def test_min_6503():
    assert min_6503(3, 7) == 3

def test_max_6504():
    assert max_6504(3, 7) == 7
