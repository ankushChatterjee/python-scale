"""Tests for test module 1438 — covers src modules [5749, 5750, 5751, 5752]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5749 import modulo_5749
from module_5750 import power_5750
from module_5751 import min_5751
from module_5752 import max_5752

def test_modulo_5749():
    assert modulo_5749(10, 3) == 1

def test_power_5750():
    assert power_5750(2, 8) == 256

def test_min_5751():
    assert min_5751(3, 7) == 3

def test_max_5752():
    assert max_5752(3, 7) == 7
