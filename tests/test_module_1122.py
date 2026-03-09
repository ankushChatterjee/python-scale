"""Tests for test module 1122 — covers src modules [4485, 4486, 4487, 4488]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4485 import modulo_4485
from module_4486 import power_4486
from module_4487 import min_4487
from module_4488 import max_4488

def test_modulo_4485():
    assert modulo_4485(10, 3) == 1

def test_power_4486():
    assert power_4486(2, 8) == 256

def test_min_4487():
    assert min_4487(3, 7) == 3

def test_max_4488():
    assert max_4488(3, 7) == 7
