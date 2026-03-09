"""Tests for test module 2382 — covers src modules [9525, 9526, 9527, 9528]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9525 import modulo_9525
from module_9526 import power_9526
from module_9527 import min_9527
from module_9528 import max_9528

def test_modulo_9525():
    assert modulo_9525(10, 3) == 1

def test_power_9526():
    assert power_9526(2, 8) == 256

def test_min_9527():
    assert min_9527(3, 7) == 3

def test_max_9528():
    assert max_9528(3, 7) == 7
