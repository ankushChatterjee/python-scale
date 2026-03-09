"""Tests for test module 360 — covers src modules [1437, 1438, 1439, 1440]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1437 import modulo_1437
from module_1438 import power_1438
from module_1439 import min_1439
from module_1440 import max_1440

def test_modulo_1437():
    assert modulo_1437(10, 3) == 1

def test_power_1438():
    assert power_1438(2, 8) == 256

def test_min_1439():
    assert min_1439(3, 7) == 3

def test_max_1440():
    assert max_1440(3, 7) == 7
