"""Tests for test module 1940 — covers src modules [7757, 7758, 7759, 7760]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7757 import modulo_7757
from module_7758 import power_7758
from module_7759 import min_7759
from module_7760 import max_7760

def test_modulo_7757():
    assert modulo_7757(10, 3) == 1

def test_power_7758():
    assert power_7758(2, 8) == 256

def test_min_7759():
    assert min_7759(3, 7) == 3

def test_max_7760():
    assert max_7760(3, 7) == 7
