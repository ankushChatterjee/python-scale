"""Tests for test module 130 — covers src modules [517, 518, 519, 520]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_517 import modulo_517
from module_518 import power_518
from module_519 import min_519
from module_520 import max_520

def test_modulo_517():
    assert modulo_517(10, 3) == 1

def test_power_518():
    assert power_518(2, 8) == 256

def test_min_519():
    assert min_519(3, 7) == 3

def test_max_520():
    assert max_520(3, 7) == 7
