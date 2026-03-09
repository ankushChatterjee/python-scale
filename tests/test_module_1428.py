"""Tests for test module 1428 — covers src modules [5709, 5710, 5711, 5712]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5709 import modulo_5709
from module_5710 import power_5710
from module_5711 import min_5711
from module_5712 import max_5712

def test_modulo_5709():
    assert modulo_5709(10, 3) == 1

def test_power_5710():
    assert power_5710(2, 8) == 256

def test_min_5711():
    assert min_5711(3, 7) == 3

def test_max_5712():
    assert max_5712(3, 7) == 7
