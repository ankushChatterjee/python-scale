"""Tests for test module 1158 — covers src modules [4629, 4630, 4631, 4632]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4629 import modulo_4629
from module_4630 import power_4630
from module_4631 import min_4631
from module_4632 import max_4632

def test_modulo_4629():
    assert modulo_4629(10, 3) == 1

def test_power_4630():
    assert power_4630(2, 8) == 256

def test_min_4631():
    assert min_4631(3, 7) == 3

def test_max_4632():
    assert max_4632(3, 7) == 7
