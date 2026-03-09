"""Tests for test module 1440 — covers src modules [5757, 5758, 5759, 5760]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5757 import modulo_5757
from module_5758 import power_5758
from module_5759 import min_5759
from module_5760 import max_5760

def test_modulo_5757():
    assert modulo_5757(10, 3) == 1

def test_power_5758():
    assert power_5758(2, 8) == 256

def test_min_5759():
    assert min_5759(3, 7) == 3

def test_max_5760():
    assert max_5760(3, 7) == 7
