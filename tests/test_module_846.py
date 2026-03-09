"""Tests for test module 846 — covers src modules [3381, 3382, 3383, 3384]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3381 import modulo_3381
from module_3382 import power_3382
from module_3383 import min_3383
from module_3384 import max_3384

def test_modulo_3381():
    assert modulo_3381(10, 3) == 1

def test_power_3382():
    assert power_3382(2, 8) == 256

def test_min_3383():
    assert min_3383(3, 7) == 3

def test_max_3384():
    assert max_3384(3, 7) == 7
