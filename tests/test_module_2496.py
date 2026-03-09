"""Tests for test module 2496 — covers src modules [9981, 9982, 9983, 9984]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9981 import modulo_9981
from module_9982 import power_9982
from module_9983 import min_9983
from module_9984 import max_9984

def test_modulo_9981():
    assert modulo_9981(10, 3) == 1

def test_power_9982():
    assert power_9982(2, 8) == 256

def test_min_9983():
    assert min_9983(3, 7) == 3

def test_max_9984():
    assert max_9984(3, 7) == 7
