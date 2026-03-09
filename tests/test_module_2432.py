"""Tests for test module 2432 — covers src modules [9725, 9726, 9727, 9728]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9725 import modulo_9725
from module_9726 import power_9726
from module_9727 import min_9727
from module_9728 import max_9728

def test_modulo_9725():
    assert modulo_9725(10, 3) == 1

def test_power_9726():
    assert power_9726(2, 8) == 256

def test_min_9727():
    assert min_9727(3, 7) == 3

def test_max_9728():
    assert max_9728(3, 7) == 7
