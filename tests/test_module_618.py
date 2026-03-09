"""Tests for test module 618 — covers src modules [2469, 2470, 2471, 2472]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2469 import modulo_2469
from module_2470 import power_2470
from module_2471 import min_2471
from module_2472 import max_2472

def test_modulo_2469():
    assert modulo_2469(10, 3) == 1

def test_power_2470():
    assert power_2470(2, 8) == 256

def test_min_2471():
    assert min_2471(3, 7) == 3

def test_max_2472():
    assert max_2472(3, 7) == 7
