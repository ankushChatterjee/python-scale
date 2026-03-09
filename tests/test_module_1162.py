"""Tests for test module 1162 — covers src modules [4645, 4646, 4647, 4648]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4645 import modulo_4645
from module_4646 import power_4646
from module_4647 import min_4647
from module_4648 import max_4648

def test_modulo_4645():
    assert modulo_4645(10, 3) == 1

def test_power_4646():
    assert power_4646(2, 8) == 256

def test_min_4647():
    assert min_4647(3, 7) == 3

def test_max_4648():
    assert max_4648(3, 7) == 7
