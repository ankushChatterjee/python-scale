"""Tests for test module 1880 — covers src modules [7517, 7518, 7519, 7520]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7517 import modulo_7517
from module_7518 import power_7518
from module_7519 import min_7519
from module_7520 import max_7520

def test_modulo_7517():
    assert modulo_7517(10, 3) == 1

def test_power_7518():
    assert power_7518(2, 8) == 256

def test_min_7519():
    assert min_7519(3, 7) == 3

def test_max_7520():
    assert max_7520(3, 7) == 7
