"""Tests for test module 1168 — covers src modules [4669, 4670, 4671, 4672]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4669 import modulo_4669
from module_4670 import power_4670
from module_4671 import min_4671
from module_4672 import max_4672

def test_modulo_4669():
    assert modulo_4669(10, 3) == 1

def test_power_4670():
    assert power_4670(2, 8) == 256

def test_min_4671():
    assert min_4671(3, 7) == 3

def test_max_4672():
    assert max_4672(3, 7) == 7
