"""Tests for test module 1618 — covers src modules [6469, 6470, 6471, 6472]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6469 import modulo_6469
from module_6470 import power_6470
from module_6471 import min_6471
from module_6472 import max_6472

def test_modulo_6469():
    assert modulo_6469(10, 3) == 1

def test_power_6470():
    assert power_6470(2, 8) == 256

def test_min_6471():
    assert min_6471(3, 7) == 3

def test_max_6472():
    assert max_6472(3, 7) == 7
