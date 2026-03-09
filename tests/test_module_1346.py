"""Tests for test module 1346 — covers src modules [5381, 5382, 5383, 5384]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5381 import modulo_5381
from module_5382 import power_5382
from module_5383 import min_5383
from module_5384 import max_5384

def test_modulo_5381():
    assert modulo_5381(10, 3) == 1

def test_power_5382():
    assert power_5382(2, 8) == 256

def test_min_5383():
    assert min_5383(3, 7) == 3

def test_max_5384():
    assert max_5384(3, 7) == 7
