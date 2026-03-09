"""Tests for test module 1086 — covers src modules [4341, 4342, 4343, 4344]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4341 import modulo_4341
from module_4342 import power_4342
from module_4343 import min_4343
from module_4344 import max_4344

def test_modulo_4341():
    assert modulo_4341(10, 3) == 1

def test_power_4342():
    assert power_4342(2, 8) == 256

def test_min_4343():
    assert min_4343(3, 7) == 3

def test_max_4344():
    assert max_4344(3, 7) == 7
