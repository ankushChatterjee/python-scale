"""Tests for test module 1692 — covers src modules [6765, 6766, 6767, 6768]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6765 import modulo_6765
from module_6766 import power_6766
from module_6767 import min_6767
from module_6768 import max_6768

def test_modulo_6765():
    assert modulo_6765(10, 3) == 1

def test_power_6766():
    assert power_6766(2, 8) == 256

def test_min_6767():
    assert min_6767(3, 7) == 3

def test_max_6768():
    assert max_6768(3, 7) == 7
