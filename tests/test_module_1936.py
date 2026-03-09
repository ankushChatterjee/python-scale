"""Tests for test module 1936 — covers src modules [7741, 7742, 7743, 7744]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7741 import modulo_7741
from module_7742 import power_7742
from module_7743 import min_7743
from module_7744 import max_7744

def test_modulo_7741():
    assert modulo_7741(10, 3) == 1

def test_power_7742():
    assert power_7742(2, 8) == 256

def test_min_7743():
    assert min_7743(3, 7) == 3

def test_max_7744():
    assert max_7744(3, 7) == 7
