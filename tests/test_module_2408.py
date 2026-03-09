"""Tests for test module 2408 — covers src modules [9629, 9630, 9631, 9632]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9629 import modulo_9629
from module_9630 import power_9630
from module_9631 import min_9631
from module_9632 import max_9632

def test_modulo_9629():
    assert modulo_9629(10, 3) == 1

def test_power_9630():
    assert power_9630(2, 8) == 256

def test_min_9631():
    assert min_9631(3, 7) == 3

def test_max_9632():
    assert max_9632(3, 7) == 7
