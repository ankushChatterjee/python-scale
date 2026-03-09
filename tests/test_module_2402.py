"""Tests for test module 2402 — covers src modules [9605, 9606, 9607, 9608]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9605 import modulo_9605
from module_9606 import power_9606
from module_9607 import min_9607
from module_9608 import max_9608

def test_modulo_9605():
    assert modulo_9605(10, 3) == 1

def test_power_9606():
    assert power_9606(2, 8) == 256

def test_min_9607():
    assert min_9607(3, 7) == 3

def test_max_9608():
    assert max_9608(3, 7) == 7
