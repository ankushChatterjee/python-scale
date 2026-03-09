"""Tests for test module 692 — covers src modules [2765, 2766, 2767, 2768]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2765 import modulo_2765
from module_2766 import power_2766
from module_2767 import min_2767
from module_2768 import max_2768

def test_modulo_2765():
    assert modulo_2765(10, 3) == 1

def test_power_2766():
    assert power_2766(2, 8) == 256

def test_min_2767():
    assert min_2767(3, 7) == 3

def test_max_2768():
    assert max_2768(3, 7) == 7
