"""Tests for test module 1442 — covers src modules [5765, 5766, 5767, 5768]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5765 import modulo_5765
from module_5766 import power_5766
from module_5767 import min_5767
from module_5768 import max_5768

def test_modulo_5765():
    assert modulo_5765(10, 3) == 1

def test_power_5766():
    assert power_5766(2, 8) == 256

def test_min_5767():
    assert min_5767(3, 7) == 3

def test_max_5768():
    assert max_5768(3, 7) == 7
