"""Tests for test module 376 — covers src modules [1501, 1502, 1503, 1504]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1501 import modulo_1501
from module_1502 import power_1502
from module_1503 import min_1503
from module_1504 import max_1504

def test_modulo_1501():
    assert modulo_1501(10, 3) == 1

def test_power_1502():
    assert power_1502(2, 8) == 256

def test_min_1503():
    assert min_1503(3, 7) == 3

def test_max_1504():
    assert max_1504(3, 7) == 7
