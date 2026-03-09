"""Tests for test module 1132 — covers src modules [4525, 4526, 4527, 4528]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4525 import modulo_4525
from module_4526 import power_4526
from module_4527 import min_4527
from module_4528 import max_4528

def test_modulo_4525():
    assert modulo_4525(10, 3) == 1

def test_power_4526():
    assert power_4526(2, 8) == 256

def test_min_4527():
    assert min_4527(3, 7) == 3

def test_max_4528():
    assert max_4528(3, 7) == 7
