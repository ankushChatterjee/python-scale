"""Tests for test module 884 — covers src modules [3533, 3534, 3535, 3536]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3533 import modulo_3533
from module_3534 import power_3534
from module_3535 import min_3535
from module_3536 import max_3536

def test_modulo_3533():
    assert modulo_3533(10, 3) == 1

def test_power_3534():
    assert power_3534(2, 8) == 256

def test_min_3535():
    assert min_3535(3, 7) == 3

def test_max_3536():
    assert max_3536(3, 7) == 7
