"""Tests for test module 2414 — covers src modules [9653, 9654, 9655, 9656]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9653 import modulo_9653
from module_9654 import power_9654
from module_9655 import min_9655
from module_9656 import max_9656

def test_modulo_9653():
    assert modulo_9653(10, 3) == 1

def test_power_9654():
    assert power_9654(2, 8) == 256

def test_min_9655():
    assert min_9655(3, 7) == 3

def test_max_9656():
    assert max_9656(3, 7) == 7
