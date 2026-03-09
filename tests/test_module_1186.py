"""Tests for test module 1186 — covers src modules [4741, 4742, 4743, 4744]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4741 import modulo_4741
from module_4742 import power_4742
from module_4743 import min_4743
from module_4744 import max_4744

def test_modulo_4741():
    assert modulo_4741(10, 3) == 1

def test_power_4742():
    assert power_4742(2, 8) == 256

def test_min_4743():
    assert min_4743(3, 7) == 3

def test_max_4744():
    assert max_4744(3, 7) == 7
