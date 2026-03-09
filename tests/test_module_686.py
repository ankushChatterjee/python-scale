"""Tests for test module 686 — covers src modules [2741, 2742, 2743, 2744]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2741 import modulo_2741
from module_2742 import power_2742
from module_2743 import min_2743
from module_2744 import max_2744

def test_modulo_2741():
    assert modulo_2741(10, 3) == 1

def test_power_2742():
    assert power_2742(2, 8) == 256

def test_min_2743():
    assert min_2743(3, 7) == 3

def test_max_2744():
    assert max_2744(3, 7) == 7
