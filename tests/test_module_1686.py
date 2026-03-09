"""Tests for test module 1686 — covers src modules [6741, 6742, 6743, 6744]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6741 import modulo_6741
from module_6742 import power_6742
from module_6743 import min_6743
from module_6744 import max_6744

def test_modulo_6741():
    assert modulo_6741(10, 3) == 1

def test_power_6742():
    assert power_6742(2, 8) == 256

def test_min_6743():
    assert min_6743(3, 7) == 3

def test_max_6744():
    assert max_6744(3, 7) == 7
