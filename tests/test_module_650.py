"""Tests for test module 650 — covers src modules [2597, 2598, 2599, 2600]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2597 import modulo_2597
from module_2598 import power_2598
from module_2599 import min_2599
from module_2600 import max_2600

def test_modulo_2597():
    assert modulo_2597(10, 3) == 1

def test_power_2598():
    assert power_2598(2, 8) == 256

def test_min_2599():
    assert min_2599(3, 7) == 3

def test_max_2600():
    assert max_2600(3, 7) == 7
