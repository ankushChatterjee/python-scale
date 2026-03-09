"""Tests for test module 1334 — covers src modules [5333, 5334, 5335, 5336]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5333 import modulo_5333
from module_5334 import power_5334
from module_5335 import min_5335
from module_5336 import max_5336

def test_modulo_5333():
    assert modulo_5333(10, 3) == 1

def test_power_5334():
    assert power_5334(2, 8) == 256

def test_min_5335():
    assert min_5335(3, 7) == 3

def test_max_5336():
    assert max_5336(3, 7) == 7
