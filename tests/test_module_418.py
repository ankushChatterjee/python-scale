"""Tests for test module 418 — covers src modules [1669, 1670, 1671, 1672]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1669 import modulo_1669
from module_1670 import power_1670
from module_1671 import min_1671
from module_1672 import max_1672

def test_modulo_1669():
    assert modulo_1669(10, 3) == 1

def test_power_1670():
    assert power_1670(2, 8) == 256

def test_min_1671():
    assert min_1671(3, 7) == 3

def test_max_1672():
    assert max_1672(3, 7) == 7
