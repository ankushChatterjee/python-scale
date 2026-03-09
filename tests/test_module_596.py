"""Tests for test module 596 — covers src modules [2381, 2382, 2383, 2384]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2381 import modulo_2381
from module_2382 import power_2382
from module_2383 import min_2383
from module_2384 import max_2384

def test_modulo_2381():
    assert modulo_2381(10, 3) == 1

def test_power_2382():
    assert power_2382(2, 8) == 256

def test_min_2383():
    assert min_2383(3, 7) == 3

def test_max_2384():
    assert max_2384(3, 7) == 7
