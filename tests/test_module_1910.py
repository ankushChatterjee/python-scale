"""Tests for test module 1910 — covers src modules [7637, 7638, 7639, 7640]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7637 import modulo_7637
from module_7638 import power_7638
from module_7639 import min_7639
from module_7640 import max_7640

def test_modulo_7637():
    assert modulo_7637(10, 3) == 1

def test_power_7638():
    assert power_7638(2, 8) == 256

def test_min_7639():
    assert min_7639(3, 7) == 3

def test_max_7640():
    assert max_7640(3, 7) == 7
