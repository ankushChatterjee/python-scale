"""Tests for test module 868 — covers src modules [3469, 3470, 3471, 3472]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3469 import modulo_3469
from module_3470 import power_3470
from module_3471 import min_3471
from module_3472 import max_3472

def test_modulo_3469():
    assert modulo_3469(10, 3) == 1

def test_power_3470():
    assert power_3470(2, 8) == 256

def test_min_3471():
    assert min_3471(3, 7) == 3

def test_max_3472():
    assert max_3472(3, 7) == 7
