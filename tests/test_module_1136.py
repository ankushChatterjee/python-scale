"""Tests for test module 1136 — covers src modules [4541, 4542, 4543, 4544]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4541 import modulo_4541
from module_4542 import power_4542
from module_4543 import min_4543
from module_4544 import max_4544

def test_modulo_4541():
    assert modulo_4541(10, 3) == 1

def test_power_4542():
    assert power_4542(2, 8) == 256

def test_min_4543():
    assert min_4543(3, 7) == 3

def test_max_4544():
    assert max_4544(3, 7) == 7
