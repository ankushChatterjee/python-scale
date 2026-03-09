"""Tests for test module 2346 — covers src modules [9381, 9382, 9383, 9384]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9381 import modulo_9381
from module_9382 import power_9382
from module_9383 import min_9383
from module_9384 import max_9384

def test_modulo_9381():
    assert modulo_9381(10, 3) == 1

def test_power_9382():
    assert power_9382(2, 8) == 256

def test_min_9383():
    assert min_9383(3, 7) == 3

def test_max_9384():
    assert max_9384(3, 7) == 7
