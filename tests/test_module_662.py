"""Tests for test module 662 — covers src modules [2645, 2646, 2647, 2648]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2645 import modulo_2645
from module_2646 import power_2646
from module_2647 import min_2647
from module_2648 import max_2648

def test_modulo_2645():
    assert modulo_2645(10, 3) == 1

def test_power_2646():
    assert power_2646(2, 8) == 256

def test_min_2647():
    assert min_2647(3, 7) == 3

def test_max_2648():
    assert max_2648(3, 7) == 7
