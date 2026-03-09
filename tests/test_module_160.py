"""Tests for test module 160 — covers src modules [637, 638, 639, 640]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_637 import modulo_637
from module_638 import power_638
from module_639 import min_639
from module_640 import max_640

def test_modulo_637():
    assert modulo_637(10, 3) == 1

def test_power_638():
    assert power_638(2, 8) == 256

def test_min_639():
    assert min_639(3, 7) == 3

def test_max_640():
    assert max_640(3, 7) == 7
