"""Tests for test module 2440 — covers src modules [9757, 9758, 9759, 9760]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9757 import modulo_9757
from module_9758 import power_9758
from module_9759 import min_9759
from module_9760 import max_9760

def test_modulo_9757():
    assert modulo_9757(10, 3) == 1

def test_power_9758():
    assert power_9758(2, 8) == 256

def test_min_9759():
    assert min_9759(3, 7) == 3

def test_max_9760():
    assert max_9760(3, 7) == 7
