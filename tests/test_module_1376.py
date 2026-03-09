"""Tests for test module 1376 — covers src modules [5501, 5502, 5503, 5504]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5501 import modulo_5501
from module_5502 import power_5502
from module_5503 import min_5503
from module_5504 import max_5504

def test_modulo_5501():
    assert modulo_5501(10, 3) == 1

def test_power_5502():
    assert power_5502(2, 8) == 256

def test_min_5503():
    assert min_5503(3, 7) == 3

def test_max_5504():
    assert max_5504(3, 7) == 7
