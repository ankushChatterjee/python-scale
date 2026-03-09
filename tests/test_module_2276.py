"""Tests for test module 2276 — covers src modules [9101, 9102, 9103, 9104]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9101 import modulo_9101
from module_9102 import power_9102
from module_9103 import min_9103
from module_9104 import max_9104

def test_modulo_9101():
    assert modulo_9101(10, 3) == 1

def test_power_9102():
    assert power_9102(2, 8) == 256

def test_min_9103():
    assert min_9103(3, 7) == 3

def test_max_9104():
    assert max_9104(3, 7) == 7
