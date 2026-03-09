"""Tests for test module 936 — covers src modules [3741, 3742, 3743, 3744]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3741 import modulo_3741
from module_3742 import power_3742
from module_3743 import min_3743
from module_3744 import max_3744

def test_modulo_3741():
    assert modulo_3741(10, 3) == 1

def test_power_3742():
    assert power_3742(2, 8) == 256

def test_min_3743():
    assert min_3743(3, 7) == 3

def test_max_3744():
    assert max_3744(3, 7) == 7
