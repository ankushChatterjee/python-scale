"""Tests for test module 190 — covers src modules [757, 758, 759, 760]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_757 import modulo_757
from module_758 import power_758
from module_759 import min_759
from module_760 import max_760

def test_modulo_757():
    assert modulo_757(10, 3) == 1

def test_power_758():
    assert power_758(2, 8) == 256

def test_min_759():
    assert min_759(3, 7) == 3

def test_max_760():
    assert max_760(3, 7) == 7
