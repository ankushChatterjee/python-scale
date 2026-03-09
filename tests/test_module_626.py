"""Tests for test module 626 — covers src modules [2501, 2502, 2503, 2504]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2501 import modulo_2501
from module_2502 import power_2502
from module_2503 import min_2503
from module_2504 import max_2504

def test_modulo_2501():
    assert modulo_2501(10, 3) == 1

def test_power_2502():
    assert power_2502(2, 8) == 256

def test_min_2503():
    assert min_2503(3, 7) == 3

def test_max_2504():
    assert max_2504(3, 7) == 7
