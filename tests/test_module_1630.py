"""Tests for test module 1630 — covers src modules [6517, 6518, 6519, 6520]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6517 import modulo_6517
from module_6518 import power_6518
from module_6519 import min_6519
from module_6520 import max_6520

def test_modulo_6517():
    assert modulo_6517(10, 3) == 1

def test_power_6518():
    assert power_6518(2, 8) == 256

def test_min_6519():
    assert min_6519(3, 7) == 3

def test_max_6520():
    assert max_6520(3, 7) == 7
