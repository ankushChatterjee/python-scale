"""Tests for test module 2190 — covers src modules [8757, 8758, 8759, 8760]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8757 import modulo_8757
from module_8758 import power_8758
from module_8759 import min_8759
from module_8760 import max_8760

def test_modulo_8757():
    assert modulo_8757(10, 3) == 1

def test_power_8758():
    assert power_8758(2, 8) == 256

def test_min_8759():
    assert min_8759(3, 7) == 3

def test_max_8760():
    assert max_8760(3, 7) == 7
