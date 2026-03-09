"""Tests for test module 2472 — covers src modules [9885, 9886, 9887, 9888]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9885 import modulo_9885
from module_9886 import power_9886
from module_9887 import min_9887
from module_9888 import max_9888

def test_modulo_9885():
    assert modulo_9885(10, 3) == 1

def test_power_9886():
    assert power_9886(2, 8) == 256

def test_min_9887():
    assert min_9887(3, 7) == 3

def test_max_9888():
    assert max_9888(3, 7) == 7
