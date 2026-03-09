"""Tests for test module 2436 — covers src modules [9741, 9742, 9743, 9744]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9741 import modulo_9741
from module_9742 import power_9742
from module_9743 import min_9743
from module_9744 import max_9744

def test_modulo_9741():
    assert modulo_9741(10, 3) == 1

def test_power_9742():
    assert power_9742(2, 8) == 256

def test_min_9743():
    assert min_9743(3, 7) == 3

def test_max_9744():
    assert max_9744(3, 7) == 7
