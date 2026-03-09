"""Tests for test module 682 — covers src modules [2725, 2726, 2727, 2728]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2725 import modulo_2725
from module_2726 import power_2726
from module_2727 import min_2727
from module_2728 import max_2728

def test_modulo_2725():
    assert modulo_2725(10, 3) == 1

def test_power_2726():
    assert power_2726(2, 8) == 256

def test_min_2727():
    assert min_2727(3, 7) == 3

def test_max_2728():
    assert max_2728(3, 7) == 7
