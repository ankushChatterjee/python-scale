"""Tests for test module 1288 — covers src modules [5149, 5150, 5151, 5152]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5149 import modulo_5149
from module_5150 import power_5150
from module_5151 import min_5151
from module_5152 import max_5152

def test_modulo_5149():
    assert modulo_5149(10, 3) == 1

def test_power_5150():
    assert power_5150(2, 8) == 256

def test_min_5151():
    assert min_5151(3, 7) == 3

def test_max_5152():
    assert max_5152(3, 7) == 7
