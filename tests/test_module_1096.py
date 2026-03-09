"""Tests for test module 1096 — covers src modules [4381, 4382, 4383, 4384]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4381 import modulo_4381
from module_4382 import power_4382
from module_4383 import min_4383
from module_4384 import max_4384

def test_modulo_4381():
    assert modulo_4381(10, 3) == 1

def test_power_4382():
    assert power_4382(2, 8) == 256

def test_min_4383():
    assert min_4383(3, 7) == 3

def test_max_4384():
    assert max_4384(3, 7) == 7
