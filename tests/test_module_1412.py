"""Tests for test module 1412 — covers src modules [5645, 5646, 5647, 5648]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5645 import modulo_5645
from module_5646 import power_5646
from module_5647 import min_5647
from module_5648 import max_5648

def test_modulo_5645():
    assert modulo_5645(10, 3) == 1

def test_power_5646():
    assert power_5646(2, 8) == 256

def test_min_5647():
    assert min_5647(3, 7) == 3

def test_max_5648():
    assert max_5648(3, 7) == 7
