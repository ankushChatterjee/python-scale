"""Tests for test module 1160 — covers src modules [4637, 4638, 4639, 4640]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4637 import modulo_4637
from module_4638 import power_4638
from module_4639 import min_4639
from module_4640 import max_4640

def test_modulo_4637():
    assert modulo_4637(10, 3) == 1

def test_power_4638():
    assert power_4638(2, 8) == 256

def test_min_4639():
    assert min_4639(3, 7) == 3

def test_max_4640():
    assert max_4640(3, 7) == 7
