"""Tests for test module 216 — covers src modules [861, 862, 863, 864]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_861 import modulo_861
from module_862 import power_862
from module_863 import min_863
from module_864 import max_864

def test_modulo_861():
    assert modulo_861(10, 3) == 1

def test_power_862():
    assert power_862(2, 8) == 256

def test_min_863():
    assert min_863(3, 7) == 3

def test_max_864():
    assert max_864(3, 7) == 7
