"""Tests for test module 2146 — covers src modules [8581, 8582, 8583, 8584]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8581 import modulo_8581
from module_8582 import power_8582
from module_8583 import min_8583
from module_8584 import max_8584

def test_modulo_8581():
    assert modulo_8581(10, 3) == 1

def test_power_8582():
    assert power_8582(2, 8) == 256

def test_min_8583():
    assert min_8583(3, 7) == 3

def test_max_8584():
    assert max_8584(3, 7) == 7
