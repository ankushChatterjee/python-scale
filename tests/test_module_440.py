"""Tests for test module 440 — covers src modules [1757, 1758, 1759, 1760]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1757 import modulo_1757
from module_1758 import power_1758
from module_1759 import min_1759
from module_1760 import max_1760

def test_modulo_1757():
    assert modulo_1757(10, 3) == 1

def test_power_1758():
    assert power_1758(2, 8) == 256

def test_min_1759():
    assert min_1759(3, 7) == 3

def test_max_1760():
    assert max_1760(3, 7) == 7
