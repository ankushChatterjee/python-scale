"""Tests for test module 2442 — covers src modules [9765, 9766, 9767, 9768]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9765 import modulo_9765
from module_9766 import power_9766
from module_9767 import min_9767
from module_9768 import max_9768

def test_modulo_9765():
    assert modulo_9765(10, 3) == 1

def test_power_9766():
    assert power_9766(2, 8) == 256

def test_min_9767():
    assert min_9767(3, 7) == 3

def test_max_9768():
    assert max_9768(3, 7) == 7
