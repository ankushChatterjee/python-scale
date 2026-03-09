"""Tests for test module 2186 — covers src modules [8741, 8742, 8743, 8744]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8741 import modulo_8741
from module_8742 import power_8742
from module_8743 import min_8743
from module_8744 import max_8744

def test_modulo_8741():
    assert modulo_8741(10, 3) == 1

def test_power_8742():
    assert power_8742(2, 8) == 256

def test_min_8743():
    assert min_8743(3, 7) == 3

def test_max_8744():
    assert max_8744(3, 7) == 7
