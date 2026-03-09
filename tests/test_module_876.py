"""Tests for test module 876 — covers src modules [3501, 3502, 3503, 3504]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3501 import modulo_3501
from module_3502 import power_3502
from module_3503 import min_3503
from module_3504 import max_3504

def test_modulo_3501():
    assert modulo_3501(10, 3) == 1

def test_power_3502():
    assert power_3502(2, 8) == 256

def test_min_3503():
    assert min_3503(3, 7) == 3

def test_max_3504():
    assert max_3504(3, 7) == 7
