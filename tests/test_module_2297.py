"""Tests for test module 2297 — covers src modules [9185, 9186, 9187, 9188]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9185 import add_9185
from module_9186 import subtract_9186
from module_9187 import multiply_9187
from module_9188 import divide_9188

def test_add_9185():
    assert add_9185(2, 3) == 5

def test_subtract_9186():
    assert subtract_9186(10, 4) == 6

def test_multiply_9187():
    assert multiply_9187(3, 7) == 21

def test_divide_9188():
    assert divide_9188(10, 2) == 5.0
