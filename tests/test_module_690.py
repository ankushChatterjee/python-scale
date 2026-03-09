"""Tests for test module 690 — covers src modules [2757, 2758, 2759, 2760]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2757 import modulo_2757
from module_2758 import power_2758
from module_2759 import min_2759
from module_2760 import max_2760

def test_modulo_2757():
    assert modulo_2757(10, 3) == 1

def test_power_2758():
    assert power_2758(2, 8) == 256

def test_min_2759():
    assert min_2759(3, 7) == 3

def test_max_2760():
    assert max_2760(3, 7) == 7
