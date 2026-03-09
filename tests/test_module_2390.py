"""Tests for test module 2390 — covers src modules [9557, 9558, 9559, 9560]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9557 import modulo_9557
from module_9558 import power_9558
from module_9559 import min_9559
from module_9560 import max_9560

def test_modulo_9557():
    assert modulo_9557(10, 3) == 1

def test_power_9558():
    assert power_9558(2, 8) == 256

def test_min_9559():
    assert min_9559(3, 7) == 3

def test_max_9560():
    assert max_9560(3, 7) == 7
