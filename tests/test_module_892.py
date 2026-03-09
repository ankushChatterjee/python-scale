"""Tests for test module 892 — covers src modules [3565, 3566, 3567, 3568]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3565 import modulo_3565
from module_3566 import power_3566
from module_3567 import min_3567
from module_3568 import max_3568

def test_modulo_3565():
    assert modulo_3565(10, 3) == 1

def test_power_3566():
    assert power_3566(2, 8) == 256

def test_min_3567():
    assert min_3567(3, 7) == 3

def test_max_3568():
    assert max_3568(3, 7) == 7
