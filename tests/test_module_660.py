"""Tests for test module 660 — covers src modules [2637, 2638, 2639, 2640]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2637 import modulo_2637
from module_2638 import power_2638
from module_2639 import min_2639
from module_2640 import max_2640

def test_modulo_2637():
    assert modulo_2637(10, 3) == 1

def test_power_2638():
    assert power_2638(2, 8) == 256

def test_min_2639():
    assert min_2639(3, 7) == 3

def test_max_2640():
    assert max_2640(3, 7) == 7
