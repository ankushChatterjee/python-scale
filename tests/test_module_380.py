"""Tests for test module 380 — covers src modules [1517, 1518, 1519, 1520]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1517 import modulo_1517
from module_1518 import power_1518
from module_1519 import min_1519
from module_1520 import max_1520

def test_modulo_1517():
    assert modulo_1517(10, 3) == 1

def test_power_1518():
    assert power_1518(2, 8) == 256

def test_min_1519():
    assert min_1519(3, 7) == 3

def test_max_1520():
    assert max_1520(3, 7) == 7
