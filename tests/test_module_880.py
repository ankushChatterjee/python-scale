"""Tests for test module 880 — covers src modules [3517, 3518, 3519, 3520]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3517 import modulo_3517
from module_3518 import power_3518
from module_3519 import min_3519
from module_3520 import max_3520

def test_modulo_3517():
    assert modulo_3517(10, 3) == 1

def test_power_3518():
    assert power_3518(2, 8) == 256

def test_min_3519():
    assert min_3519(3, 7) == 3

def test_max_3520():
    assert max_3520(3, 7) == 7
