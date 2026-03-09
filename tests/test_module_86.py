"""Tests for test module 86 — covers src modules [341, 342, 343, 344]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_341 import modulo_341
from module_342 import power_342
from module_343 import min_343
from module_344 import max_344

def test_modulo_341():
    assert modulo_341(10, 3) == 1

def test_power_342():
    assert power_342(2, 8) == 256

def test_min_343():
    assert min_343(3, 7) == 3

def test_max_344():
    assert max_344(3, 7) == 7
