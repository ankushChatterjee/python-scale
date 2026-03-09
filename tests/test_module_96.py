"""Tests for test module 96 — covers src modules [381, 382, 383, 384]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_381 import modulo_381
from module_382 import power_382
from module_383 import min_383
from module_384 import max_384

def test_modulo_381():
    assert modulo_381(10, 3) == 1

def test_power_382():
    assert power_382(2, 8) == 256

def test_min_383():
    assert min_383(3, 7) == 3

def test_max_384():
    assert max_384(3, 7) == 7
