"""Tests for test module 1134 — covers src modules [4533, 4534, 4535, 4536]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4533 import modulo_4533
from module_4534 import power_4534
from module_4535 import min_4535
from module_4536 import max_4536

def test_modulo_4533():
    assert modulo_4533(10, 3) == 1

def test_power_4534():
    assert power_4534(2, 8) == 256

def test_min_4535():
    assert min_4535(3, 7) == 3

def test_max_4536():
    assert max_4536(3, 7) == 7
