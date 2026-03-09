"""Tests for test module 766 — covers src modules [3061, 3062, 3063, 3064]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3061 import modulo_3061
from module_3062 import power_3062
from module_3063 import min_3063
from module_3064 import max_3064

def test_modulo_3061():
    assert modulo_3061(10, 3) == 1

def test_power_3062():
    assert power_3062(2, 8) == 256

def test_min_3063():
    assert min_3063(3, 7) == 3

def test_max_3064():
    assert max_3064(3, 7) == 7
