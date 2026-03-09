"""Tests for test module 2296 — covers src modules [9181, 9182, 9183, 9184]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9181 import modulo_9181
from module_9182 import power_9182
from module_9183 import min_9183
from module_9184 import max_9184

def test_modulo_9181():
    assert modulo_9181(10, 3) == 1

def test_power_9182():
    assert power_9182(2, 8) == 256

def test_min_9183():
    assert min_9183(3, 7) == 3

def test_max_9184():
    assert max_9184(3, 7) == 7
