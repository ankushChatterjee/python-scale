"""Tests for test module 2416 — covers src modules [9661, 9662, 9663, 9664]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9661 import modulo_9661
from module_9662 import power_9662
from module_9663 import min_9663
from module_9664 import max_9664

def test_modulo_9661():
    assert modulo_9661(10, 3) == 1

def test_power_9662():
    assert power_9662(2, 8) == 256

def test_min_9663():
    assert min_9663(3, 7) == 3

def test_max_9664():
    assert max_9664(3, 7) == 7
