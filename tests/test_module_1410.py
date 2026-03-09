"""Tests for test module 1410 — covers src modules [5637, 5638, 5639, 5640]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5637 import modulo_5637
from module_5638 import power_5638
from module_5639 import min_5639
from module_5640 import max_5640

def test_modulo_5637():
    assert modulo_5637(10, 3) == 1

def test_power_5638():
    assert power_5638(2, 8) == 256

def test_min_5639():
    assert min_5639(3, 7) == 3

def test_max_5640():
    assert max_5640(3, 7) == 7
