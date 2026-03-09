"""Tests for test module 442 — covers src modules [1765, 1766, 1767, 1768]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1765 import modulo_1765
from module_1766 import power_1766
from module_1767 import min_1767
from module_1768 import max_1768

def test_modulo_1765():
    assert modulo_1765(10, 3) == 1

def test_power_1766():
    assert power_1766(2, 8) == 256

def test_min_1767():
    assert min_1767(3, 7) == 3

def test_max_1768():
    assert max_1768(3, 7) == 7
