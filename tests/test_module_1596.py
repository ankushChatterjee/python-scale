"""Tests for test module 1596 — covers src modules [6381, 6382, 6383, 6384]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6381 import modulo_6381
from module_6382 import power_6382
from module_6383 import min_6383
from module_6384 import max_6384

def test_modulo_6381():
    assert modulo_6381(10, 3) == 1

def test_power_6382():
    assert power_6382(2, 8) == 256

def test_min_6383():
    assert min_6383(3, 7) == 3

def test_max_6384():
    assert max_6384(3, 7) == 7
