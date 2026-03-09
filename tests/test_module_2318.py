"""Tests for test module 2318 — covers src modules [9269, 9270, 9271, 9272]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9269 import modulo_9269
from module_9270 import power_9270
from module_9271 import min_9271
from module_9272 import max_9272

def test_modulo_9269():
    assert modulo_9269(10, 3) == 1

def test_power_9270():
    assert power_9270(2, 8) == 256

def test_min_9271():
    assert min_9271(3, 7) == 3

def test_max_9272():
    assert max_9272(3, 7) == 7
