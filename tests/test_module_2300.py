"""Tests for test module 2300 — covers src modules [9197, 9198, 9199, 9200]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9197 import modulo_9197
from module_9198 import power_9198
from module_9199 import min_9199
from module_9200 import max_9200

def test_modulo_9197():
    assert modulo_9197(10, 3) == 1

def test_power_9198():
    assert power_9198(2, 8) == 256

def test_min_9199():
    assert min_9199(3, 7) == 3

def test_max_9200():
    assert max_9200(3, 7) == 7
