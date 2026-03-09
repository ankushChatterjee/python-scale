"""Tests for test module 1564 — covers src modules [6253, 6254, 6255, 6256]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6253 import modulo_6253
from module_6254 import power_6254
from module_6255 import min_6255
from module_6256 import max_6256

def test_modulo_6253():
    assert modulo_6253(10, 3) == 1

def test_power_6254():
    assert power_6254(2, 8) == 256

def test_min_6255():
    assert min_6255(3, 7) == 3

def test_max_6256():
    assert max_6256(3, 7) == 7
