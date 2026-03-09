"""Tests for test module 2092 — covers src modules [8365, 8366, 8367, 8368]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8365 import modulo_8365
from module_8366 import power_8366
from module_8367 import min_8367
from module_8368 import max_8368

def test_modulo_8365():
    assert modulo_8365(10, 3) == 1

def test_power_8366():
    assert power_8366(2, 8) == 256

def test_min_8367():
    assert min_8367(3, 7) == 3

def test_max_8368():
    assert max_8368(3, 7) == 7
