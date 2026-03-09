"""Tests for test module 1606 — covers src modules [6421, 6422, 6423, 6424]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6421 import modulo_6421
from module_6422 import power_6422
from module_6423 import min_6423
from module_6424 import max_6424

def test_modulo_6421():
    assert modulo_6421(10, 3) == 1

def test_power_6422():
    assert power_6422(2, 8) == 256

def test_min_6423():
    assert min_6423(3, 7) == 3

def test_max_6424():
    assert max_6424(3, 7) == 7
