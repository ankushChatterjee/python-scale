"""Tests for test module 1942 — covers src modules [7765, 7766, 7767, 7768]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7765 import modulo_7765
from module_7766 import power_7766
from module_7767 import min_7767
from module_7768 import max_7768

def test_modulo_7765():
    assert modulo_7765(10, 3) == 1

def test_power_7766():
    assert power_7766(2, 8) == 256

def test_min_7767():
    assert min_7767(3, 7) == 3

def test_max_7768():
    assert max_7768(3, 7) == 7
