"""Tests for test module 436 — covers src modules [1741, 1742, 1743, 1744]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1741 import modulo_1741
from module_1742 import power_1742
from module_1743 import min_1743
from module_1744 import max_1744

def test_modulo_1741():
    assert modulo_1741(10, 3) == 1

def test_power_1742():
    assert power_1742(2, 8) == 256

def test_min_1743():
    assert min_1743(3, 7) == 3

def test_max_1744():
    assert max_1744(3, 7) == 7
