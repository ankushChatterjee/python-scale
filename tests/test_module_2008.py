"""Tests for test module 2008 — covers src modules [8029, 8030, 8031, 8032]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8029 import modulo_8029
from module_8030 import power_8030
from module_8031 import min_8031
from module_8032 import max_8032

def test_modulo_8029():
    assert modulo_8029(10, 3) == 1

def test_power_8030():
    assert power_8030(2, 8) == 256

def test_min_8031():
    assert min_8031(3, 7) == 3

def test_max_8032():
    assert max_8032(3, 7) == 7
