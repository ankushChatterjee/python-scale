"""Tests for test module 2168 — covers src modules [8669, 8670, 8671, 8672]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8669 import modulo_8669
from module_8670 import power_8670
from module_8671 import min_8671
from module_8672 import max_8672

def test_modulo_8669():
    assert modulo_8669(10, 3) == 1

def test_power_8670():
    assert power_8670(2, 8) == 256

def test_min_8671():
    assert min_8671(3, 7) == 3

def test_max_8672():
    assert max_8672(3, 7) == 7
