"""Tests for test module 2316 — covers src modules [9261, 9262, 9263, 9264]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9261 import modulo_9261
from module_9262 import power_9262
from module_9263 import min_9263
from module_9264 import max_9264

def test_modulo_9261():
    assert modulo_9261(10, 3) == 1

def test_power_9262():
    assert power_9262(2, 8) == 256

def test_min_9263():
    assert min_9263(3, 7) == 3

def test_max_9264():
    assert max_9264(3, 7) == 7
