"""Tests for test module 2273 — covers src modules [9089, 9090, 9091, 9092]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9089 import add_9089
from module_9090 import subtract_9090
from module_9091 import multiply_9091
from module_9092 import divide_9092

def test_add_9089():
    assert add_9089(2, 3) == 5

def test_subtract_9090():
    assert subtract_9090(10, 4) == 6

def test_multiply_9091():
    assert multiply_9091(3, 7) == 21

def test_divide_9092():
    assert divide_9092(10, 2) == 5.0
