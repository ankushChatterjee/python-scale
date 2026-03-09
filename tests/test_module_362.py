"""Tests for test module 362 — covers src modules [1445, 1446, 1447, 1448]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1445 import modulo_1445
from module_1446 import power_1446
from module_1447 import min_1447
from module_1448 import max_1448

def test_modulo_1445():
    assert modulo_1445(10, 3) == 1

def test_power_1446():
    assert power_1446(2, 8) == 256

def test_min_1447():
    assert min_1447(3, 7) == 3

def test_max_1448():
    assert max_1448(3, 7) == 7
