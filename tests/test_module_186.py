"""Tests for test module 186 — covers src modules [741, 742, 743, 744]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_741 import modulo_741
from module_742 import power_742
from module_743 import min_743
from module_744 import max_744

def test_modulo_741():
    assert modulo_741(10, 3) == 1

def test_power_742():
    assert power_742(2, 8) == 256

def test_min_743():
    assert min_743(3, 7) == 3

def test_max_744():
    assert max_744(3, 7) == 7
