"""Tests for test module 918 — covers src modules [3669, 3670, 3671, 3672]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3669 import modulo_3669
from module_3670 import power_3670
from module_3671 import min_3671
from module_3672 import max_3672

def test_modulo_3669():
    assert modulo_3669(10, 3) == 1

def test_power_3670():
    assert power_3670(2, 8) == 256

def test_min_3671():
    assert min_3671(3, 7) == 3

def test_max_3672():
    assert max_3672(3, 7) == 7
