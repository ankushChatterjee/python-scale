"""Tests for test module 1690 — covers src modules [6757, 6758, 6759, 6760]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6757 import modulo_6757
from module_6758 import power_6758
from module_6759 import min_6759
from module_6760 import max_6760

def test_modulo_6757():
    assert modulo_6757(10, 3) == 1

def test_power_6758():
    assert power_6758(2, 8) == 256

def test_min_6759():
    assert min_6759(3, 7) == 3

def test_max_6760():
    assert max_6760(3, 7) == 7
