"""Tests for test module 2320 — covers src modules [9277, 9278, 9279, 9280]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9277 import modulo_9277
from module_9278 import power_9278
from module_9279 import min_9279
from module_9280 import max_9280

def test_modulo_9277():
    assert modulo_9277(10, 3) == 1

def test_power_9278():
    assert power_9278(2, 8) == 256

def test_min_9279():
    assert min_9279(3, 7) == 3

def test_max_9280():
    assert max_9280(3, 7) == 7
