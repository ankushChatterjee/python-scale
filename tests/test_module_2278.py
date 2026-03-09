"""Tests for test module 2278 — covers src modules [9109, 9110, 9111, 9112]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9109 import modulo_9109
from module_9110 import power_9110
from module_9111 import min_9111
from module_9112 import max_9112

def test_modulo_9109():
    assert modulo_9109(10, 3) == 1

def test_power_9110():
    assert power_9110(2, 8) == 256

def test_min_9111():
    assert min_9111(3, 7) == 3

def test_max_9112():
    assert max_9112(3, 7) == 7
