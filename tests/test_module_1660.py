"""Tests for test module 1660 — covers src modules [6637, 6638, 6639, 6640]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6637 import modulo_6637
from module_6638 import power_6638
from module_6639 import min_6639
from module_6640 import max_6640

def test_modulo_6637():
    assert modulo_6637(10, 3) == 1

def test_power_6638():
    assert power_6638(2, 8) == 256

def test_min_6639():
    assert min_6639(3, 7) == 3

def test_max_6640():
    assert max_6640(3, 7) == 7
