"""Tests for test module 154 — covers src modules [613, 614, 615, 616]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_613 import modulo_613
from module_614 import power_614
from module_615 import min_615
from module_616 import max_616

def test_modulo_613():
    assert modulo_613(10, 3) == 1

def test_power_614():
    assert power_614(2, 8) == 256

def test_min_615():
    assert min_615(3, 7) == 3

def test_max_616():
    assert max_616(3, 7) == 7
