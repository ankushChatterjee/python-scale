"""Tests for test module 2418 — covers src modules [9669, 9670, 9671, 9672]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9669 import modulo_9669
from module_9670 import power_9670
from module_9671 import min_9671
from module_9672 import max_9672

def test_modulo_9669():
    assert modulo_9669(10, 3) == 1

def test_power_9670():
    assert power_9670(2, 8) == 256

def test_min_9671():
    assert min_9671(3, 7) == 3

def test_max_9672():
    assert max_9672(3, 7) == 7
