"""Tests for test module 384 — covers src modules [1533, 1534, 1535, 1536]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1533 import modulo_1533
from module_1534 import power_1534
from module_1535 import min_1535
from module_1536 import max_1536

def test_modulo_1533():
    assert modulo_1533(10, 3) == 1

def test_power_1534():
    assert power_1534(2, 8) == 256

def test_min_1535():
    assert min_1535(3, 7) == 3

def test_max_1536():
    assert max_1536(3, 7) == 7
