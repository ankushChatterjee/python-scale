"""Tests for test module 940 — covers src modules [3757, 3758, 3759, 3760]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3757 import modulo_3757
from module_3758 import power_3758
from module_3759 import min_3759
from module_3760 import max_3760

def test_modulo_3757():
    assert modulo_3757(10, 3) == 1

def test_power_3758():
    assert power_3758(2, 8) == 256

def test_min_3759():
    assert min_3759(3, 7) == 3

def test_max_3760():
    assert max_3760(3, 7) == 7
