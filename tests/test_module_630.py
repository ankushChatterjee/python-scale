"""Tests for test module 630 — covers src modules [2517, 2518, 2519, 2520]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2517 import modulo_2517
from module_2518 import power_2518
from module_2519 import min_2519
from module_2520 import max_2520

def test_modulo_2517():
    assert modulo_2517(10, 3) == 1

def test_power_2518():
    assert power_2518(2, 8) == 256

def test_min_2519():
    assert min_2519(3, 7) == 3

def test_max_2520():
    assert max_2520(3, 7) == 7
