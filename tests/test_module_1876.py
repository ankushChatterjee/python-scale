"""Tests for test module 1876 — covers src modules [7501, 7502, 7503, 7504]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7501 import modulo_7501
from module_7502 import power_7502
from module_7503 import min_7503
from module_7504 import max_7504

def test_modulo_7501():
    assert modulo_7501(10, 3) == 1

def test_power_7502():
    assert power_7502(2, 8) == 256

def test_min_7503():
    assert min_7503(3, 7) == 3

def test_max_7504():
    assert max_7504(3, 7) == 7
