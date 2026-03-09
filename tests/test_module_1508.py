"""Tests for test module 1508 — covers src modules [6029, 6030, 6031, 6032]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6029 import modulo_6029
from module_6030 import power_6030
from module_6031 import min_6031
from module_6032 import max_6032

def test_modulo_6029():
    assert modulo_6029(10, 3) == 1

def test_power_6030():
    assert power_6030(2, 8) == 256

def test_min_6031():
    assert min_6031(3, 7) == 3

def test_max_6032():
    assert max_6032(3, 7) == 7
