"""Tests for test module 1418 — covers src modules [5669, 5670, 5671, 5672]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5669 import modulo_5669
from module_5670 import power_5670
from module_5671 import min_5671
from module_5672 import max_5672

def test_modulo_5669():
    assert modulo_5669(10, 3) == 1

def test_power_5670():
    assert power_5670(2, 8) == 256

def test_min_5671():
    assert min_5671(3, 7) == 3

def test_max_5672():
    assert max_5672(3, 7) == 7
