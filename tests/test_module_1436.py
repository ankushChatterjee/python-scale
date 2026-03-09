"""Tests for test module 1436 — covers src modules [5741, 5742, 5743, 5744]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5741 import modulo_5741
from module_5742 import power_5742
from module_5743 import min_5743
from module_5744 import max_5744

def test_modulo_5741():
    assert modulo_5741(10, 3) == 1

def test_power_5742():
    assert power_5742(2, 8) == 256

def test_min_5743():
    assert min_5743(3, 7) == 3

def test_max_5744():
    assert max_5744(3, 7) == 7
