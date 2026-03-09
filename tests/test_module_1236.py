"""Tests for test module 1236 — covers src modules [4941, 4942, 4943, 4944]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4941 import modulo_4941
from module_4942 import power_4942
from module_4943 import min_4943
from module_4944 import max_4944

def test_modulo_4941():
    assert modulo_4941(10, 3) == 1

def test_power_4942():
    assert power_4942(2, 8) == 256

def test_min_4943():
    assert min_4943(3, 7) == 3

def test_max_4944():
    assert max_4944(3, 7) == 7
