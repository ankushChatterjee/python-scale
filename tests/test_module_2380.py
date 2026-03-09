"""Tests for test module 2380 — covers src modules [9517, 9518, 9519, 9520]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9517 import modulo_9517
from module_9518 import power_9518
from module_9519 import min_9519
from module_9520 import max_9520

def test_modulo_9517():
    assert modulo_9517(10, 3) == 1

def test_power_9518():
    assert power_9518(2, 8) == 256

def test_min_9519():
    assert min_9519(3, 7) == 3

def test_max_9520():
    assert max_9520(3, 7) == 7
