"""Tests for test module 1584 — covers src modules [6333, 6334, 6335, 6336]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6333 import modulo_6333
from module_6334 import power_6334
from module_6335 import min_6335
from module_6336 import max_6336

def test_modulo_6333():
    assert modulo_6333(10, 3) == 1

def test_power_6334():
    assert power_6334(2, 8) == 256

def test_min_6335():
    assert min_6335(3, 7) == 3

def test_max_6336():
    assert max_6336(3, 7) == 7
