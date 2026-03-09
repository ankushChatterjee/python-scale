"""Tests for test module 942 — covers src modules [3765, 3766, 3767, 3768]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3765 import modulo_3765
from module_3766 import power_3766
from module_3767 import min_3767
from module_3768 import max_3768

def test_modulo_3765():
    assert modulo_3765(10, 3) == 1

def test_power_3766():
    assert power_3766(2, 8) == 256

def test_min_3767():
    assert min_3767(3, 7) == 3

def test_max_3768():
    assert max_3768(3, 7) == 7
