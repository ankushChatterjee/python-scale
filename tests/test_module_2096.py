"""Tests for test module 2096 — covers src modules [8381, 8382, 8383, 8384]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8381 import modulo_8381
from module_8382 import power_8382
from module_8383 import min_8383
from module_8384 import max_8384

def test_modulo_8381():
    assert modulo_8381(10, 3) == 1

def test_power_8382():
    assert power_8382(2, 8) == 256

def test_min_8383():
    assert min_8383(3, 7) == 3

def test_max_8384():
    assert max_8384(3, 7) == 7
