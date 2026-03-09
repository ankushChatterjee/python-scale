"""Tests for test module 1008 — covers src modules [4029, 4030, 4031, 4032]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4029 import modulo_4029
from module_4030 import power_4030
from module_4031 import min_4031
from module_4032 import max_4032

def test_modulo_4029():
    assert modulo_4029(10, 3) == 1

def test_power_4030():
    assert power_4030(2, 8) == 256

def test_min_4031():
    assert min_4031(3, 7) == 3

def test_max_4032():
    assert max_4032(3, 7) == 7
