"""Tests for test module 2306 — covers src modules [9221, 9222, 9223, 9224]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9221 import modulo_9221
from module_9222 import power_9222
from module_9223 import min_9223
from module_9224 import max_9224

def test_modulo_9221():
    assert modulo_9221(10, 3) == 1

def test_power_9222():
    assert power_9222(2, 8) == 256

def test_min_9223():
    assert min_9223(3, 7) == 3

def test_max_9224():
    assert max_9224(3, 7) == 7
