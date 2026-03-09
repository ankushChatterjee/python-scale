"""Tests for test module 2410 — covers src modules [9637, 9638, 9639, 9640]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9637 import modulo_9637
from module_9638 import power_9638
from module_9639 import min_9639
from module_9640 import max_9640

def test_modulo_9637():
    assert modulo_9637(10, 3) == 1

def test_power_9638():
    assert power_9638(2, 8) == 256

def test_min_9639():
    assert min_9639(3, 7) == 3

def test_max_9640():
    assert max_9640(3, 7) == 7
