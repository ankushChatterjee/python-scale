"""Tests for test module 622 — covers src modules [2485, 2486, 2487, 2488]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2485 import modulo_2485
from module_2486 import power_2486
from module_2487 import min_2487
from module_2488 import max_2488

def test_modulo_2485():
    assert modulo_2485(10, 3) == 1

def test_power_2486():
    assert power_2486(2, 8) == 256

def test_min_2487():
    assert min_2487(3, 7) == 3

def test_max_2488():
    assert max_2488(3, 7) == 7
