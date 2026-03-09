"""Tests for test module 1220 — covers src modules [4877, 4878, 4879, 4880]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4877 import modulo_4877
from module_4878 import power_4878
from module_4879 import min_4879
from module_4880 import max_4880

def test_modulo_4877():
    assert modulo_4877(10, 3) == 1

def test_power_4878():
    assert power_4878(2, 8) == 256

def test_min_4879():
    assert min_4879(3, 7) == 3

def test_max_4880():
    assert max_4880(3, 7) == 7
