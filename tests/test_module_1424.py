"""Tests for test module 1424 — covers src modules [5693, 5694, 5695, 5696]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5693 import modulo_5693
from module_5694 import power_5694
from module_5695 import min_5695
from module_5696 import max_5696

def test_modulo_5693():
    assert modulo_5693(10, 3) == 1

def test_power_5694():
    assert power_5694(2, 8) == 256

def test_min_5695():
    assert min_5695(3, 7) == 3

def test_max_5696():
    assert max_5696(3, 7) == 7
