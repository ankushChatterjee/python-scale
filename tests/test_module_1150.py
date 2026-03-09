"""Tests for test module 1150 — covers src modules [4597, 4598, 4599, 4600]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4597 import modulo_4597
from module_4598 import power_4598
from module_4599 import min_4599
from module_4600 import max_4600

def test_modulo_4597():
    assert modulo_4597(10, 3) == 1

def test_power_4598():
    assert power_4598(2, 8) == 256

def test_min_4599():
    assert min_4599(3, 7) == 3

def test_max_4600():
    assert max_4600(3, 7) == 7
