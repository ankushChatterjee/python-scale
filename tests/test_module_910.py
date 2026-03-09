"""Tests for test module 910 — covers src modules [3637, 3638, 3639, 3640]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3637 import modulo_3637
from module_3638 import power_3638
from module_3639 import min_3639
from module_3640 import max_3640

def test_modulo_3637():
    assert modulo_3637(10, 3) == 1

def test_power_3638():
    assert power_3638(2, 8) == 256

def test_min_3639():
    assert min_3639(3, 7) == 3

def test_max_3640():
    assert max_3640(3, 7) == 7
