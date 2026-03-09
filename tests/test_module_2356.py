"""Tests for test module 2356 — covers src modules [9421, 9422, 9423, 9424]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9421 import modulo_9421
from module_9422 import power_9422
from module_9423 import min_9423
from module_9424 import max_9424

def test_modulo_9421():
    assert modulo_9421(10, 3) == 1

def test_power_9422():
    assert power_9422(2, 8) == 256

def test_min_9423():
    assert min_9423(3, 7) == 3

def test_max_9424():
    assert max_9424(3, 7) == 7
